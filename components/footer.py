import streamlit as st

def footer_home():
    st.markdown(f"""
        <div style="text-align:center; gap:6px; margin-top:2rem display:flex;  justify-content:center">
        <p style="font-weight:bold; color:white;">Created with ❤️ by Harsh Mishra</p>
        </div>
    """, unsafe_allow_html=True)