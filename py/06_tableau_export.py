import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\02 - SaaS Sales Funnel Analysis\pipeline.db")

# Pull everything we need for the dashboard, with a few calculated fields baked in
df = pd.read_sql("""
    SELECT
        [Opportunity ID],
        Technology,
        City,
        [B2B Sales Medium],
        [Sales Velocity],
        [Opportunity Status],
        [Sales Stage Iterations],
        [Opportunity Size (USD)],
        [Client Revenue Sizing],
        [Client Employee Sizing],
        [Business from Client Last Year],
        [Compete Intel],
        [Opportunity Sizing],
        Won,
        CASE WHEN Won = 1 THEN [Opportunity Size (USD)] ELSE 0 END AS Won_Revenue,
        CASE WHEN Won = 0 THEN [Opportunity Size (USD)] ELSE 0 END AS Lost_Revenue
    FROM opportunities
""", conn)

# Export
df.to_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\02 - SaaS Sales Funnel Analysis\csv\pipeline_tableau.csv", index=False)
print(f"Tableau export complete. Rows: {len(df)}")
conn.close()