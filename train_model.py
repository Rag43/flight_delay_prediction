import sqlite3
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#Connect to SQLite db
conn = sqlite3.connect("flights.db")
df = pd.read_sql_query("SELECT * FROM flights", conn)
conn.close()

# Convert categorical variables to numerical (one-hot encoding)
df = pd.get_dummies(df, columns=["airline", "origin", "destination"], drop_first=True)
df_sample = df.sample(frac=0.1, random_state=42)


#Create a "weekday" feature (Monday = 0; Sunday = 6)
df["weekday"] = pd.to_datetime(df[["year", "month", "day"]]).dt.weekday

#Define features (x) and target (y)
x = df_sample.drop(columns=["departure_delay", "year"])
y = (df_sample["departure_delay"] > 15).astype(int) # 1 - delayed; 0 - On Time; target var

#Split data into training (80%) and testing (20%) sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train.shape, y_train.shape)

print("Checking for NaN values in training data...")
print(x_train.isnull().sum())
print(y_train.isnull().sum())

# Train the random forest model with 100 trees
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

#Save feature names
feature_names = list(x_train.columns)

with open("flight_delay_model.pkl", "wb") as file:
    pickle.dump((model, feature_names), file)

print("Model and feature names saved!")

#Get feature importance scores
importances = model.feature_importances_
feature_names = x_train.columns
feature_importance = sorted(zip(feature_names, importances),
                             key=lambda x: x[1], reverse=True)
print("\nFeature importance ranking:")
for feature, importance in feature_importance:
    print(f"{feature}: {importance:.4f}")

# Extract feature names and importance scores
features, importances = zip(*feature_importance)

#Group feature importances for categories
grouped_importance = {}
for feature, importance in zip(features, importances):
    if feature.startswith("origin_"):
        grouped_importance["origin"] = grouped_importance.get("origin", 0) + importance
    elif feature.startswith("destination_"):
        grouped_importance["destination"] = grouped_importance.get("destination", 0) + importance
    elif feature.startswith("airline_"):
        grouped_importance["airline"] = grouped_importance.get("airline", 0) + importance
    else:
        grouped_importance[feature] = importance

#Convert to a sorted list
sorted_features = sorted(grouped_importance.items(), key=lambda x:x[1], reverse=True)

#Extract names and scores for plotting
grouped_features, grouped_importances = zip(*sorted_features)

plt.figure(figsize=(8, 5))
plt.barh(grouped_features, grouped_importances, color="skyblue")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Feature Importance in Flight Delay Prediction")
plt.gca().invert_yaxis() # highest importance on top
plt.show()

#Make predictions
y_pred = model.predict(x_test)

#check model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")


