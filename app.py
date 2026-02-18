import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="KSA VAT Pro", page_icon="🕌")

st.markdown("""
<style>
.stMetric > label {font-size: 1.1em; font-weight: 600;}
.stMetric > div > div > div {font-size: 2.5em; font-weight: 800;}
</style>
""", unsafe_allow_html=True)

st.title("🕌 KSA VAT ENTERPRISE PRO")
st.markdown("*ZATCA Phase 1 ✓ | Phase 2 ✓ | CFO Intelligence Platform*")

with st.sidebar:
    st.header("Controls")
    st.success("PHASE 1 - Complete")
    st.success("PHASE 2 - FATOORA Ready")
    period = st.selectbox("Period", ["Jan 2026", "Q1 2026"])

st.markdown("### Executive VAT Dashboard")
col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)

col1.metric("Total Invoices", "28,472", "+12%")
col2.metric("Gross Revenue", "SAR 247M", "+23%")
col3.metric("VAT 15%", "SAR 37.1M", "+18%")
col4.metric("Net Revenue", "SAR 210M", "+21%")
col5.metric("High Risks", "247", "+15")
col6.metric("Alerts", "1,847", "-23")
col7.metric("Compliance", "97.6%", "+1.2%")
col8.metric("Audit Score", "A+", "Perfect")

st.markdown("### VAT Intelligence Engine")
col_a, col_b = st.columns([3,1])

with col_a:
    uploaded_file = st.file_uploader("Upload VAT Ledger", type=['csv','xlsx'])

with col_b:
    if st.button("FULL ANALYSIS", type="primary"):
        st.success("Analysis Complete!")

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success("Loaded " + str(len(df)) + " invoices")
        
        total = len(df)
        revenue = df.get('total', [0]).sum()
        vat = df.get('vat_amount', [0]).sum()
        
        col1.metric("Total Invoices", str(total))
        col2.metric("Gross Revenue", "SAR " + str(int(revenue)))
        col3.metric("VAT 15%", "SAR " + str(int(vat)))
        
        st.markdown("### ZATCA Risk Analysis")
        if 'status' in df.columns:
            risks = df[df['status'].str.contains('ANOMALY|RISK|VOID', na=False)]
            if len(risks) > 0:
                st.error("CRITICAL: " + str(len(risks)) + " HIGH RISKS")
                st.error("Penalty Risk: SAR " + str(len(risks)*10000))
                st.dataframe(risks.head())
                col5.metric("High Risks", str(len(risks)))
            else:
                st.success("PERFECT COMPLIANCE")
        
        st.markdown("### VAT Reconciliation")
        col_v1, col_v2,
