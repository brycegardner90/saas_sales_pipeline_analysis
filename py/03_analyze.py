import pandas as pd

df = pd.read_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\02 - SaaS Sales Funnel Analysis\csv\pipeline_cleaned.csv")

# ── OVERALL WIN RATE ──────────────────────────────────────
overall_win_rate = df['Won'].mean() * 100
print(f"=== OVERALL WIN RATE ===")
print(f"{overall_win_rate:.1f}%")

# ── WIN RATE BY SALES CHANNEL ─────────────────────────────
print("\n=== WIN RATE BY B2B SALES MEDIUM ===")
win_by_channel = df.groupby('B2B Sales Medium')['Won'].agg(['count', 'mean'])
win_by_channel['mean'] = (win_by_channel['mean'] * 100).round(1)
win_by_channel.columns = ['total_opportunities', 'win_rate_pct']
print(win_by_channel.sort_values('win_rate_pct', ascending=False))

# ── WIN RATE BY TECHNOLOGY ────────────────────────────────
print("\n=== WIN RATE BY TECHNOLOGY ===")
win_by_tech = df.groupby('Technology')['Won'].agg(['count', 'mean'])
win_by_tech['mean'] = (win_by_tech['mean'] * 100).round(1)
win_by_tech.columns = ['total_opportunities', 'win_rate_pct']
print(win_by_tech.sort_values('win_rate_pct', ascending=False))

# ── WIN RATE BY OPPORTUNITY SIZE ──────────────────────────
print("\n=== WIN RATE BY OPPORTUNITY SIZE ===")
win_by_size = df.groupby('Opportunity Sizing')['Won'].agg(['count', 'mean'])
win_by_size['mean'] = (win_by_size['mean'] * 100).round(1)
win_by_size.columns = ['total_opportunities', 'win_rate_pct']
print(win_by_size.sort_values('win_rate_pct', ascending=False))

# ── WIN RATE BY COMPETE INTEL ──────────────────────────────
print("\n=== WIN RATE BY COMPETE INTEL ===")
win_by_compete = df.groupby('Compete Intel')['Won'].agg(['count', 'mean'])
win_by_compete['mean'] = (win_by_compete['mean'] * 100).round(1)
win_by_compete.columns = ['total_opportunities', 'win_rate_pct']
print(win_by_compete.sort_values('win_rate_pct', ascending=False))

# ── WIN RATE BY CLIENT REVENUE SIZE ───────────────────────
print("\n=== WIN RATE BY CLIENT REVENUE SIZING ===")
win_by_revenue = df.groupby('Client Revenue Sizing')['Won'].agg(['count', 'mean'])
win_by_revenue['mean'] = (win_by_revenue['mean'] * 100).round(1)
win_by_revenue.columns = ['total_opportunities', 'win_rate_pct']
print(win_by_revenue.sort_values('win_rate_pct', ascending=False))

# ── SALES STAGE ITERATIONS: WON VS LOST ───────────────────
print("\n=== AVG SALES STAGE ITERATIONS: WON VS LOST ===")
iterations_comparison = df.groupby('Won')['Sales Stage Iterations'].mean().round(2)
iterations_comparison.index = ['Lost', 'Won']
print(iterations_comparison)

# ── SALES VELOCITY: WON VS LOST ───────────────────────────
print("\n=== AVG SALES VELOCITY: WON VS LOST ===")
velocity_comparison = df.groupby('Won')['Sales Velocity'].mean().round(2)
velocity_comparison.index = ['Lost', 'Won']
print(velocity_comparison)

# Save for SQL phase
df.to_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\02 - SaaS Sales Funnel Analysis\csv\pipeline_analyzed.csv", index=False)
print("\nAnalyzed file saved.")