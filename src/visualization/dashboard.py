
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Revenue Leakage & CLV Analytics", layout="wide")
df = pd.read_csv("data/enterprise_telecom_revenue_data.csv")

st.title("Enterprise Revenue Leakage & CLV Analytics Platform")

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue Leakage", f"₹{df.revenue_leakage.sum():,.0f}")
col2.metric("Avg Leakage %", f"{(df.revenue_leakage.sum()/df.base_revenue.sum())*100:.2f}%")
col3.metric("Churn Rate", f"{df.churned.mean()*100:.2f}%")

st.subheader("Revenue Leakage by Root Cause (₹ Impact)")

root_cause_data = {
    "Billing Errors": df.loc[df["billing_error_flag"] == 1, "revenue_leakage"].sum(),
    "High Complaints": df.loc[df["complaints_count"] > 3, "revenue_leakage"].sum(),
    "Heavy Discounts": df.loc[df["discount_pct"] >= 20, "revenue_leakage"].sum(),
    "Late Payments": df.loc[df["late_payment_flag"] == 1, "revenue_leakage"].sum()
}

root_df = (
    pd.DataFrame.from_dict(root_cause_data, orient="index", columns=["Revenue Leakage"])
    .sort_values("Revenue Leakage", ascending=False)
)

st.bar_chart(root_df)

st.subheader("Revenue Leakage by Root Cause (₹ Impact)")

root_cause_data = {
    "Billing Errors": df.loc[df["billing_error_flag"] == 1, "revenue_leakage"].sum(),
    "High Complaints": df.loc[df["complaints_count"] > 3, "revenue_leakage"].sum(),
    "Heavy Discounts": df.loc[df["discount_pct"] >= 20, "revenue_leakage"].sum(),
    "Late Payments": df.loc[df["late_payment_flag"] == 1, "revenue_leakage"].sum()
}

root_df = (
    pd.DataFrame.from_dict(root_cause_data, orient="index", columns=["Revenue Leakage"])
    .sort_values("Revenue Leakage", ascending=False)
)

st.bar_chart(root_df)

