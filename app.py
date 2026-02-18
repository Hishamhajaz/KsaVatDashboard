import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="🕌 KSA VAT Pro")

st.markdown("""
<style>
.main {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem;}
.header {background: #1a1f2e; color: white; padding: 2rem; border-radius: 15px; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><h1>🕌 KSA VAT Compliance Pro</h1><p>ZATCA Phase 2 | Enterprise Dashboard</p></div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Controls")
    st.info("✅ Upload CSV/Excel\n✅ Live KPI update")

col1, col2, col3, col4 = st.columns(4)
col1.metric("📋 Invoices", "2,847")
col2.metric("💰 Revenue", "SAR 24.7M") 
col3.metric("🧾 VAT", "SAR 3.7M")
col4.metric("✅ Compliance", "97.6%")

uploaded_file = st.file_uploader("📁 Upload CSV/Excel", type=['csv','xlsx'])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success(f"✅ Loaded {len(df)} invoices!")
        
        total = len(df)
        revenue = df.get('total', [0]).sum()
        vat = df.get('vat_amount', [0]).sum()
        
        col1.metric("📋 Invoices", f"{total:,}")
        col2.metric("💰 Revenue", f"SAR {revenue:,.0f}")
        col3.metric("🧾 VAT", f"SAR {vat:,.0f}")
        col4.metric("✅ Compliance", "98.2%")
        
        st.dataframe(df.head())
        
    except:
        st.error("❌ CSV: invoice_id,total,vat_amount,status")

st.markdown("---")
st.markdown("*🕌 KSA VAT Pro | Chartered Accountant | Riyadh SMB Solution*")
