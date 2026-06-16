import pandas as pd
import sqlite3

df = pd.read_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\02 - SaaS Sales Funnel Analysis\csv\pipeline_analyzed.csv")

# Create (or connect to) a SQLite database in your project folder
conn = sqlite3.connect(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\02 - SaaS Sales Funnel Analysis\pipeline.db")

# Load the dataframe into a table called 'opportunities'
df.to_sql('opportunities', conn, if_exists='replace', index=False)

print("Database created and table loaded.")
print(f"Rows loaded: {len(df)}")

# Quick sanity check
check = pd.read_sql("SELECT * FROM opportunities LIMIT 5", conn)
print("\n=== FIRST 5 ROWS FROM SQL ===")
print(check)

conn.close()