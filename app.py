import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="🕌 KSA VAT Enterprise", page_icon="🕌")

# ═══════════════════════════════════════════════════════════════
# EXECUTIVE PREMIUM CSS - CFO BOARDROOM QUALITY
st.markdown("""
<style>
/* SUPREME EXECUTIVE THEME */
.main-header { 
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 50%, #1e40af 100%);
    padding: 3.5rem 2rem; 
    border-radius: 25px; 
    color: white; 
    margin-bottom: 2.5rem;
    box-shadow: 0 25px 50px rgba(30,58,138,0.4);
    border: 1px solid rgba(255,255,255,0.1);
}
.kpi-card {
    background: rgba(255,255,255,0.95) !important;
    padding: 2rem 1.5rem !important;
    border-radius: 20px !important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1) !important;
    border: none !important;
    text-align: center;
    transition: all 0.3s ease;
    height: 140px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.kpi-card:hover { transform: translateY(-5px); box-shadow: 0 25px 50px rgba(0,0,0,0.2); }
.kpi-icon { font-size: 2.5em; margin-bottom: 0.5rem; }
.kpi-value { font-size: 2.2em; font-weight: 800; margin: 0; }
.kpi-label { font-size: 0.9em; color: #64748b; font-weight: 500; margin: 0.25rem 0 0 0; }
.kpi-trend { font-size: 0.85em; margin-top: 0.25rem; }
.trend-up { color: #10b981; }
.trend-down { color: #ef4444; }
.risk-card { border-left: 6px solid #f59e0b !important; }
.critical-card { border-left: 6px solid #ef4444 !important; }
.status-card { background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 1.5rem; border-radius: 15px; }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# EXECUTIVE HEADER - BOARDROOM QUALITY
st.markdown("""
<div class="main-header">
    <div style="text-align: center;">
        <h1 style="font-size: 3.8em; font-weight: 900; margin: 0; text-shadow: 0 2px 10px rgba(0,0,0,0.3);">🕌 KSA VAT ENTERPRISE</h1>
        <p style="font-size: 1.8em; margin: 1rem 0 0.5rem 0; font-weight: 400; opacity: 0.95;">
            ZATCA Phase 1 ✓ | Phase 2 ✓ | Real-time CFO Platform
        </p>
        <div style="font-size: 1.2em; display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap;">
            <span>🇸🇦 Riyadh Compliance Solution</span>
            <span>💰 SAR 10M+ Annual Protection</span>
            <span>📊 15% VAT Intelligence</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# CFO ENTERPRISE SIDEBAR
with st.sidebar:
    st.markdown("### 🎛️ Executive Cont
