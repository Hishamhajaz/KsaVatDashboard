import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="KSA VAT Reporter", page_icon="🕌")

# EXECUTIVE HEADER
st.markdown("""
<div style='background-color: #0e1117; padding: 30px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1)'>
    <h1 style='margin: 0; font-size: 3em; font-weight: bold;'>🕌 KSA VAT Compliance Platform</h1>
    <p style='margin: 15px 0; font-size: 1.4em; opacity: 0.9;'>ZATCA Phase 2 | E-Invoicing | Real-time Audit Protection</p>
    <p style='margin: 0; font-size: 1.1em;'>Trusted by Riyadh SMBs | 15% VAT Automated</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
