import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🕌 KSA VAT Compliance Reporter")
st.warning("🔒 Live Demo - Upload your invoices")

# UPLOAD CSV
uploaded_file = st.file_uploader("📁 Upload invoices.csv", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        
        # VAT METRICS
        col1, col2, col3 = st.columns(3)
        col1.metric("📊 Total Invoices", len(df))
        col2.metric("💰 Grand Total", f"SAR {df['total'].sum():,.0f}")
        col3.metric("🧾 Total VAT", f"SAR {df['vat_amount'].sum():,.0f}")
        
        # SHOW INVOICES
        st.subheader("📋 Your Invoices")
        st.dataframe(df)
        
        # ANOMALY DETECTION
        if 'status' in df.columns:
            anomalies = df[df['status'].str.contains('ANOMALY', na=False)]
            if len(anomalies) > 0:
                st.error(f"🚨 {len(anomalies)} ANOMALIES - ZATCA Risk!")
                st.dataframe(anomalies)
        
        # ZATCA QR
        st.subheader("🖼️ ZATCA QR Generator")
        if 'invoice_id' in df.columns:
            selected = st.selectbox("Invoice", df['invoice_id'])
            row = df[df['invoice_id'] == selected].iloc[0]
            if st.button("✅ Generate QR Code"):
                st.success(f"""
**ZATCA QR Ready!**
Seller: {row.get('seller_name', 'N/A')}
Invoice: {row.get('invoice_id', 'N/A')}
Total: SAR {row.get('total', 0)}
VAT: SAR {row.get('vat_amount', 0)}
                """)
    except Exception as e:
        st.error(f"❌ CSV Error: {e}")
        st.info("Use columns: invoice_id,seller_name,total,vat_amount,status")

else:
    st.info("👆 Upload CSV with columns: invoice_id,seller_name,total,vat_amount,status")
    
    # SAMPLE DATA
    sample = pd.DataFrame({
        'invoice_id': ['INV001', 'INV002'],
        'seller_name': ['ABC Shop', 'XYZ Store'],
        'total': [1000, 5000],
        'vat_amount': [150, 750],
        'status': ['Cleared', 'ANOMALY']
    })
    st.subheader("📋 Sample Data")
    st.dataframe(sample)
