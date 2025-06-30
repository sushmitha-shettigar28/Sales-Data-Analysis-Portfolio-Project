# load_to_db.py
import pandas as pd
import sqlite3

# Read the cleaned CSV file
df = pd.read_csv('cleaned_sales_data.csv')

# Create a connection to a new SQLite database
# If the db doesn't exist, it will be created.
conn = sqlite3.connect('sales_database.db')

# Write the data from the DataFrame to a table named 'sales' in the database
# 'if_exists='replace'' means it will drop the table first if it exists and create a new one
df.to_sql('sales', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("Data successfully loaded into sales_database.db")