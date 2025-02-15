import sqlite3

# Connect to sqlite db
conn = sqlite3.connect("flights.db")
cursor = conn.cursor()

# Fetch first 5 rows
cursor.execute("SELECT * FROM flights LIMIT 5")
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

#Close connection
conn.close()