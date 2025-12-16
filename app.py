import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Lead Scoring Agent",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown(
    """
    <h1 style='text-align: center;'>AI-Powered Lead Scoring Dashboard</h1>
    <p style='text-align: center; color: gray;'>
    Rule-Based + Machine Learning Scoring
    </p>
    """,
    unsafe_allow_html=True
)

# ---------- LOAD DATA ----------
df = pd.read_csv("data/processed/final_ranked_leads.csv")

# ---------- SIDEBAR FILTERS ----------
st.sidebar.header("🔍 Filters")

score_column = "final_score" if "final_score" in df.columns else "propensity_score"

min_score = st.sidebar.slider(
    "Minimum Final Score",
    0, 100, 60
)

location_filter = st.sidebar.multiselect(
    "Person Location",
    options=sorted(df["person_location"].unique())
)

filtered = df[df[score_column] >= min_score]

if location_filter:
    filtered = filtered[filtered["person_location"].isin(location_filter)]

# ---------- METRICS ----------
col1, col2, col3 = st.columns(3)

col1.metric("Total Leads", len(df))
col2.metric("High-Intent Leads", len(filtered))
col3.metric(
    "Avg Final Score",
    round(filtered[score_column].mean(), 2) if len(filtered) else 0
)

st.divider()

# ---------- TABLE ----------
st.subheader("Ranked Leads")

display_columns = [
    "rank",
    "name",
    "job_title",          
    "company",
    "person_location",
    "funding_stage",
    "email"
]

if "rule_score" in df.columns:
    display_columns.append("rule_score")
if "ml_score" in df.columns:
    display_columns.append("ml_score")

display_columns.append(score_column)

st.dataframe(
    filtered[display_columns],
    use_container_width=True
)

# ---------- FOOTER ----------
st.markdown(
    "<p style='text-align:center; color:gray;'>Reproducible demo · No scraped data · Assignment submission</p>",
    unsafe_allow_html=True
)
