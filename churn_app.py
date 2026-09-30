import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# FILE PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

PREDICTION_FILE = BASE_DIR / "churn_predictions.csv"


# ============================================================
# TITLE
# ============================================================

st.title("📊 Customer Churn Prediction")
st.write("Tuned XGBoost Customer Churn Predictions")


# ============================================================
# LOAD PREDICTIONS
# ============================================================

if not PREDICTION_FILE.exists():
    st.error("churn_predictions.csv was not found in the repository.")
    st.stop()

prediction_results = pd.read_csv(PREDICTION_FILE)


# ============================================================
# SUMMARY
# ============================================================

st.subheader("Prediction Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Customers",
    len(prediction_results)
)

col2.metric(
    "Predicted Churners",
    int(prediction_results["Churn_Prediction"].sum())
)

col3.metric(
    "Predicted Non-Churners",
    int((prediction_results["Churn_Prediction"] == 0).sum())
)


# ============================================================
# PREDICTION TABLE
# ============================================================

st.subheader("Customer Churn Predictions")

st.dataframe(
    prediction_results,
    use_container_width=True
)


# ============================================================
# DOWNLOAD
# ============================================================

st.subheader("Download Predictions")

csv_data = prediction_results.to_csv(index=False)

st.download_button(
    label="⬇️ Download Churn Predictions",
    data=csv_data,
    file_name="churn_predictions.csv",
    mime="text/csv"
)
