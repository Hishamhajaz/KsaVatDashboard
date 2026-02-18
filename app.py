import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🕌 KSA VAT Compliance Reporter")
st.warning("🔒 Live Demo - Upload your invoices")

# UPLOAD CSV
uploaded_file = st.file_uploader("📁 Upload invoices.csv", type="csv")

if uploaded_file is not None:
    df
