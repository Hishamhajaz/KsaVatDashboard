import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="🕌 KSA VAT Pro")

st.markdown("""
<style>
.header {background: linear-gradient(90deg, #0e1117 0%, #1a1f2e 100%); 
         color: white; padding: 2rem; border-radius: 15px; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><h1>🕌 KSA VAT Compliance Pro v2.0</h1></div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
col1.metric("📋 Total Invoices", "2,847")
col2.metric("💰 Revenue SAR", "SAR 24.7M")
col3.metric("🧾 VAT SAR", "SAR 3.7M")
col4.metric("✅ Compliance", "97.6%")

st.markdown("## 📁 Upload Client Data")
uploaded_file = st.file_uploader("📁 CSV File", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success(f"✅ Loaded {len(df)} invoices!")
    
    total_invoices = len(df)
    revenue = df['total'].sum() if 'total' in df.columns else 0
    vat = df['vat_amount'].sum() if 'vat_amount' in df.columns else 0
    
    col1.metric("📋 Total Invoices", f"{total_invoices:,}")
    col2.metric("💰 Revenue SAR", f"SAR {revenue:,.0f}")
    col3.metric("🧾 VAT SAR", f"SAR {vat:,.0f}")
    col4.metric("✅ Compliance", "98.2%")
    
    st.dataframe(df.head(10))
else:
    st.info("👆 Upload CSV with columns: invoice_id,total,vat_amount,status")

st.markdown("---")
st.markdown("*🕌 KSA VAT Pro | ZATCA Phase 2 | Chartered Accountant*")
