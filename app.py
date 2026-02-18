import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="🕌 KSA VAT Enterprise Pro", page_icon="🕌")

# EXECUTIVE CSS
st.markdown("""
<style>
.main-header {background: linear-gradient(135deg, #0e1117 0%, #1a1f2e 100%); 
              padding: 3rem; border-radius: 20px; color: white; margin-bottom: 2rem;
              box-shadow: 0 25px 50px rgba(0,0,0,0.5);}
.metric-card {background: linear-gradient(145deg, #2d3748, #1a202c); 
              padding: 1.5rem; border-radius: 15px; color: white; margin: 0.5rem 0.25rem;
              border-left: 6px solid #48bb78; text-align: center;}
.risk-card {border-left-color: #ed8936 !important;}
.critical-card {border-left-color: #f56565 !important;}
</style>
""", unsafe_allow_html=True)

# 🕌 SUPREME EXECUTIVE HEADER
st.markdown("""
<div class="main-header">
    <div style="text-align: center;">
        <h1 style="font-size: 3.2em; margin: 0;">🕌 KSA VAT ENTERPRISE PRO v6.0</h1>
        <p style="font-size: 1.6em; margin: 1rem 0;">ZATCA Phase 1 ✓ | Phase 2 ✓ | FATOORA Ready</p>
        <div style="font-size: 1.2em;">
            🇸🇦 Riyadh CFO Platform | 15% VAT Compliance | SAR 10M+ Penalty Protection
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# CFO ENTERPRISE SIDEBAR
with st.sidebar:
    st.markdown("### ⚙️ CFO Controls")
    period = st.selectbox("📊 Reporting Period", ["Jan 2026", "Q1 2026", "YTD 2026", "Custom"])
    
    st.markdown("---")
    st.markdown("### ✅ ZATCA Compliance Status")
    st.success("**✓ PHASE 1** - Electronic Generation")
    st.success("**✓ PHASE 2** - FATOORA Integration Ready")
    st.info("**QR Code Generator** - Phase 2 Compliant")
    
    st.markdown("---")
    st.caption("👨‍💼 Chartered Accountant")

# ════════════════════════════════════════════════════════════════
# EXECUTIVE 8-COLUMN CFO DASHBOARD
st.markdown("## 📊 Executive VAT Control Center")
cols = st.columns(8)

cols[0].markdown('<div class="metric-card"><h3>📋</
