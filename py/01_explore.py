import pandas as pd

df = pd.read_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\02 - SaaS Sales Funnel Analysis\csv\Sales_Pipeline_SaaS_Startup.csv")

print("=== SHAPE ===")
print(df.shape)

print("\n=== COLUMNS ===")
print(df.columns.tolist())

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== OPPORTUNITY STATUS VALUE COUNTS ===")
print(df['Opportunity Status'].value_counts())