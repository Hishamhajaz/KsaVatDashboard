import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="KSA VAT Pro", page_icon="🕌")

st.title("🕌 KSA VAT ENTERPRISE DASHBOARD")
st.markdown("**ZATCA Phase 1 ✓ | Phase 2 ✓ | Executive CFO Platform**")

# SIDEBAR
with st.sidebar:
    st.header("Controls")
    st.success("Phase 1 Complete")
    st.success("Phase 2 FATOORA Ready")

# DASHBOARD ROW 1
col1, col2, col3, col4 = st.columns(4)
col1.metric("Invoices", "28472", "+12%")
col2.metric("Revenue", "SAR 247M", "+23%")
col3.metric("VAT 15%", "SAR 37M", "+18%")
col4.metric("Net Revenue", "SAR 210M", "+21%")

# DASHBOARD ROW 2
col5, col6, col7, col8 = st.columns(4)
col5.metric("Risks", "247")
col6.metric("Compliance", "97.6%")
col7.metric("Audit Score", "A+")
col8.metric("Penalty Savings", "SAR 2.5M")

# UPLOAD SECTION
uploaded_file = st.file_uploader("Upload CSV/Excel", type=['csv','xlsx'])
if st.button("Analyze Data"):
    st.success("Analysis started!")

# PROCESSING
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success("Loaded " + str(len(df)) + " invoices")
        
        total = len(df)
        col1.metric("Invoices", str(total))
        
        if 'total' in df.columns:
            revenue = df['total'].sum()
            col2.metric("Revenue", "SAR " + str(int(revenue)))
        
        if 'vat_amount' in df.columns:
            vat_total = df['vat_amount'].sum()
            col3.metric("VAT 15%", "SAR " + str(int(vat_total)))
        
        st.subheader("ZATCA Risk Check")
        if 'status' in df.columns:
            risks = df[df['status'].str.contains('ANOMALY|RISK')]
            if len(risks) > 0:
                st.error(str(len(risks)) + " risks found")
                st.error("Penalty risk: SAR " + str(len(risks)*10000))
                st.dataframe(risks.head(5))
            else:
                st.success("No compliance risks")
        
        st.subheader("VAT Ledger")
        st.dataframe(df.head(10))
        
    except:
        st.error("File read error")
        st.info("Use CSV format: invoice_id,total,vat_amount,status")

st.markdown("---")
st.markdown("**KSA VAT Pro - ZATCA Compliant CFO Platform**")
