# Enterprise Revenue Leakage & Customer Lifetime Value (CLV) Analytics Platform

## Overview
This project simulates an **enterprise-grade analytics platform** designed to diagnose **revenue decline without a proportional increase in churn**.  
It focuses on identifying **hidden revenue leakage**, quantifying **customer lifetime value (CLV) impact**, and translating analytics into **executive-level financial decisions**.

The system mirrors how **Revenue Assurance, Finance Analytics, and Product Analytics teams** operate inside large telecom or SaaS organizations.

---

## Business Problem
Leadership observed a steady decline in revenue while churn metrics remained stable.

**Key questions addressed:**
- Where is revenue silently leaking?
- What operational issues are driving financial loss?
- Which customer segments are at highest long-term revenue risk?
- What is the potential revenue uplift if leakage drivers are fixed?

---

## Key KPIs
- **Total Revenue Leakage (₹)**
- **Average Revenue Leakage %**
- **Revenue at Risk by Root Cause**
- **Customer Lifetime Value (CLV) Distribution**
- **Churn Rate (contextual, not primary driver)**

---

## Data Description
A large, realistic **enterprise-style dataset (150,000+ customers)** is synthetically generated to resemble internal telecom/SaaS data.

**Data domains include:**
- Customer tenure and usage behavior
- Pricing plans and discount governance
- Billing errors and late payments
- Customer complaints and support interactions
- Revenue leakage and net realized revenue
- Churn indicators

Dataset location:
data/enterprise_telecom_revenue_data.csv

---

## Analytics & Data Science Work
### 1. Data Validation & Cleaning
- Revenue consistency checks
- Leakage bounds validation
- Flag normalization for operational issues

### 2. Feature Engineering
- Revenue leakage percentage
- High-risk operational flags (billing, discounts, complaints)
- CLV calculation using tenure and net revenue
- Value-based customer segmentation

### 3. Root-Cause Analysis
- Billing errors
- Heavy discounting
- Late payments
- High complaint volumes

Each root cause is quantified in **monetary impact (₹)** for finance readability.

### 4. Customer Segmentation
Customers are segmented into:
- Low Value
- Mid Value
- High Value
- Premium

This enables prioritization of **revenue protection efforts**.

### 5. Machine Learning (Supporting Analysis)
A classification model is used to identify **revenue-risk customers**, complementing descriptive and diagnostic analytics.

---

## Dashboard (Streamlit)
An executive-ready Streamlit dashboard provides:
- High-level KPIs for leadership
- Revenue leakage breakdown by root cause
- CLV distribution across customer segments
- Clear, finance-focused visual storytelling
- <img width="1918" height="1048" alt="image" src="https://github.com/user-attachments/assets/25fcb696-1cf7-4321-9952-e7db419adc7a" />
<img width="1913" height="1067" alt="image" src="https://github.com/user-attachments/assets/96951d18-5edb-4008-bb06-6d040e1aeb9b" />



---

## Project Structure
enterprise-revenue-leakage-clv/
│
├── data/
│ └── enterprise_telecom_revenue_data.csv
│
├── src/
│ ├── data/
│ │ └── data_loader.py
│ ├── features/
│ │ └── feature_engineering.py
│ ├── models/
│ │ └── train_model.py
│ ├── visualization/
│ │ └── dashboard.py
│ └── utils/
│ └── logger.py
│
├── requirements.txt
├── README.md
└── .gitignore

---

## How to Run Locally (Windows / Linux)
```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
streamlit run src/visualization/dashboard.py
The app will be available at:
http://localhost:8501

Deployment

The application is deployed using Streamlit Community Cloud with a GitHub-based workflow.

Deployment entry file:
src/visualization/dashboard.py

---




