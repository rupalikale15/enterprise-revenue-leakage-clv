
import pandas as pd

def engineer_features(df):
    df = df.copy()
    df["revenue_leakage_pct"] = df["revenue_leakage"] / df["base_revenue"]
    df["high_complaint_flag"] = (df["complaints_count"] > 3).astype(int)
    df["value_segment"] = pd.qcut(df["net_revenue"], q=4, labels=["Low","Mid","High","Premium"])
    return df
