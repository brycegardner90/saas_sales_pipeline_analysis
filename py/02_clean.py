import pandas as pd

df = pd.read_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\02 - SaaS Sales Funnel Analysis\csv\Sales_Pipeline_SaaS_Startup.csv")

# ── CLEANING ────────────────────────────────────────────

# Rename the awkward column name (has a literal newline in it)
df = df.rename(columns={'Technology\nPrimary': 'Technology'})

# Fill missing Compete Intel with 'Unknown' — blank just means untracked, not actually missing data
df['Compete Intel'] = df['Compete Intel'].fillna('Unknown')

# Create a clean binary Won flag (1 = Won, 0 = Loss) — easier to average for win rate
df['Won'] = (df['Opportunity Status'] == 'Won').astype(int)

# Confirm everything looks right
print("=== CLEANED COLUMNS ===")
print(df.columns.tolist())

print("\n=== MISSING VALUES (should be all 0 now) ===")
print(df.isnull().sum())

print("\n=== WON FLAG CHECK ===")
print(df['Won'].value_counts())

print("\n=== FINAL SHAPE ===")
print(df.shape)

# Save cleaned file
df.to_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\02 - SaaS Sales Funnel Analysis\csv\pipeline_cleaned.csv", index=False)
print("\nCleaned file saved.")