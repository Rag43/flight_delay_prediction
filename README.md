# Flight Delay Prediction System

A machine learning-based web application that predicts flight delays using historical flight data from the Bureau of Transportation Statistics (BTS).

## 🚀 Overview

This project implements a complete machine learning pipeline for predicting flight delays. It includes data preprocessing, model training, and a web-based prediction interface built with Streamlit.

## 📁 Project Structure

```
flight_delay_prediction/
├── app.py                 # Streamlit web application
├── train_model.py         # Model training script
├── load_bts_data.py       # Data loading and database setup
├── inspect_data.py        # Data inspection and cleaning
├── Jan_24.csv            # Raw BTS flight data
├── Jan_24_cleaned.csv    # Cleaned dataset (generated)
├── flights.db            # SQLite database (generated)
├── flight_delay_model.pkl # Trained model (generated)
└── README.md             # This documentation
```

## 🛠️ Features

- **Data Processing**: Automated cleaning and preprocessing of BTS flight data
- **Machine Learning Model**: Random Forest classifier for delay prediction
- **Web Interface**: User-friendly Streamlit app for making predictions
- **Database Storage**: SQLite database for efficient data management
- **Feature Analysis**: Comprehensive feature importance analysis

## 📊 Data Source

The project uses flight data from the Bureau of Transportation Statistics (BTS) for January 2024. The dataset includes:
- Flight information (airline, flight number, origin, destination)
- Temporal features (year, month, day, departure time)
- Flight characteristics (distance, departure delay)

## 🚀 Quick Start

### Prerequisites

Install the required Python packages:

```bash
pip install streamlit pandas scikit-learn matplotlib sqlite3
```

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flight_delay_prediction
   ```

2. **Data Preparation**
   ```bash
   python inspect_data.py
   python load_bts_data.py
   ```

3. **Train the Model**
   ```bash
   python train_model.py
   ```

4. **Run the Web Application**
   ```bash
   streamlit run app.py
   ```

## 📋 Usage

### Data Inspection (`inspect_data.py`)
- Loads and inspects the raw BTS dataset
- Removes rows with missing departure times
- Fills missing delay values with 0
- Saves cleaned data as `Jan_24_cleaned.csv`

### Data Loading (`load_bts_data.py`)
- Creates SQLite database (`flights.db`)
- Loads cleaned data into the database
- Sets up proper table schema for flight data

### Model Training (`train_model.py`)
- Loads data from SQLite database
- Performs feature engineering (one-hot encoding, weekday calculation)
- Trains Random Forest classifier
- Saves model and feature names to `flight_delay_model.pkl`
- Generates feature importance analysis
- Evaluates model accuracy

### Web Application (`app.py`)
- Provides interactive web interface
- Accepts user input for flight parameters
- Makes real-time delay predictions
- Displays prediction results

## 🎯 Model Details

### Algorithm
- **Random Forest Classifier** with 100 trees
- Binary classification: Delayed (>15 minutes) vs On Time

### Features Used
- **Temporal**: Month, Day, Departure Time, Weekday
- **Flight Info**: Airline, Origin Airport, Destination Airport
- **Physical**: Distance

### Performance
- Model accuracy is evaluated on a 20% test set
- Feature importance analysis provides insights into key predictors

## 🔧 Configuration

### Model Parameters
- **Test Split**: 20% of data for testing
- **Random State**: 42 (for reproducibility)
- **Sample Size**: 10% of total dataset for training (due to memory constraints)

### Prediction Threshold
- Flights with departure delays > 15 minutes are classified as "Delayed"
- Flights with delays ≤ 15 minutes are classified as "On Time"

## 📈 Feature Importance

The model analyzes feature importance to identify key predictors of flight delays:
- Origin and destination airports
- Airline carriers
- Temporal factors (month, day, time)
- Flight distance

## 🌐 Web Interface

The Streamlit app provides:
- Input fields for flight parameters
- Real-time prediction functionality
- Clear display of prediction results
- User-friendly interface

### Input Parameters
- **Month**: 1-12
- **Day**: 1-31
- **Departure Time**: HHMM format (0-2359)
- **Distance**: Flight distance in miles (50-5000)

## 🔍 Data Processing Pipeline

1. **Raw Data**: `Jan_24.csv` (BTS format)
2. **Cleaning**: Remove missing values, fill delays
3. **Database**: Store in SQLite for efficient access
4. **Feature Engineering**: One-hot encoding, temporal features
5. **Model Training**: Random Forest classifier
6. **Prediction**: Web interface for real-time predictions

## 📝 Requirements

- Python 3.7+
- pandas
- scikit-learn
- streamlit
- matplotlib
- sqlite3

