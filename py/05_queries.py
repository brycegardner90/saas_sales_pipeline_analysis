import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\02 - SaaS Sales Funnel Analysis\pipeline.db")

# ── QUERY 1: OVERALL WIN RATE & PIPELINE VALUE ───────────
print("=== Q1: OVERALL WIN RATE & PIPELINE VALUE ===")
q1 = pd.read_sql("""
    SELECT
        COUNT(*) AS total_opportunities,
        SUM(Won) AS total_won,
        ROUND(AVG(Won) * 100, 1) AS win_rate_pct,
        SUM([Opportunity Size (USD)]) AS total_pipeline_value,
        SUM(CASE WHEN Won = 1 THEN [Opportunity Size (USD)] ELSE 0 END) AS won_revenue
    FROM opportunities
""", conn)
print(q1)

# ── QUERY 2: WIN RATE & REVENUE BY SALES CHANNEL ─────────
print("\n=== Q2: WIN RATE & REVENUE BY SALES CHANNEL ===")
q2 = pd.read_sql("""
    SELECT
        [B2B Sales Medium],
        COUNT(*) AS total_opportunities,
        ROUND(AVG(Won) * 100, 1) AS win_rate_pct,
        SUM(CASE WHEN Won = 1 THEN [Opportunity Size (USD)] ELSE 0 END) AS won_revenue,
        ROUND(AVG(CASE WHEN Won = 1 THEN [Opportunity Size (USD)] ELSE NULL END), 2) AS avg_deal_size_won
    FROM opportunities
    GROUP BY [B2B Sales Medium]
    ORDER BY win_rate_pct DESC
""", conn)
print(q2)

# ── QUERY 3: REVENUE EFFICIENCY — WON REVENUE PER OPPORTUNITY WORKED ──
print("\n=== Q3: WON REVENUE PER OPPORTUNITY BY CHANNEL ===")
q3 = pd.read_sql("""
    SELECT
        [B2B Sales Medium],
        COUNT(*) AS total_opportunities,
        SUM(CASE WHEN Won = 1 THEN [Opportunity Size (USD)] ELSE 0 END) AS won_revenue,
        ROUND(SUM(CASE WHEN Won = 1 THEN [Opportunity Size (USD)] ELSE 0 END) * 1.0 / COUNT(*), 2) AS revenue_per_opportunity
    FROM opportunities
    GROUP BY [B2B Sales Medium]
    ORDER BY revenue_per_opportunity DESC
""", conn)
print(q3)

# ── QUERY 4: WIN RATE BY DEAL SIZE BUCKET ────────────────
print("\n=== Q4: WIN RATE BY OPPORTUNITY SIZE ===")
q4 = pd.read_sql("""
    SELECT
        [Opportunity Sizing],
        COUNT(*) AS total_opportunities,
        ROUND(AVG(Won) * 100, 1) AS win_rate_pct
    FROM opportunities
    GROUP BY [Opportunity Sizing]
    ORDER BY win_rate_pct DESC
""", conn)
print(q4)

# ── QUERY 5: COMPETITIVE DEALS — WIN RATE BY CHANNEL ─────
print("\n=== Q5: WIN RATE BY CHANNEL, SPLIT BY COMPETE INTEL ===")
q5 = pd.read_sql("""
    SELECT
        [B2B Sales Medium],
        [Compete Intel],
        COUNT(*) AS total_opportunities,
        ROUND(AVG(Won) * 100, 1) AS win_rate_pct
    FROM opportunities
    GROUP BY [B2B Sales Medium], [Compete Intel]
    ORDER BY [B2B Sales Medium], win_rate_pct DESC
""", conn)
print(q5)

# ── QUERY 6: TECHNOLOGY PERFORMANCE — VOLUME VS WIN RATE ──
print("\n=== Q6: TECHNOLOGY — VOLUME, WIN RATE, AND REVENUE ===")
q6 = pd.read_sql("""
    SELECT
        Technology,
        COUNT(*) AS total_opportunities,
        ROUND(AVG(Won) * 100, 1) AS win_rate_pct,
        SUM(CASE WHEN Won = 1 THEN [Opportunity Size (USD)] ELSE 0 END) AS won_revenue
    FROM opportunities
    GROUP BY Technology
    ORDER BY won_revenue DESC
""", conn)
print(q6)

conn.close()
print("\nAll queries complete.")