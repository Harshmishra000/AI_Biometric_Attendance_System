import streamlit as st
from components.header import header_home
from ui.base_layout import style_base_layout, style_background_home
from components.footer import footer_home

def home_screen():

    header_home()
    style_background_home()
    style_base_layout()

    col1,col2 = st.columns(2, gap="large")
    with col1:
          st.markdown("<h2 style='color:black;'>I'm</br> Student</h2>", unsafe_allow_html=True)
          st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=140)
          if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']= 'student'
            st.rerun()

    with col2:
        st.markdown("<h2 style='color:black;'>I'm</br> Teacher</h2>", unsafe_allow_html=True)
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']= 'teacher', 
            st.rerun()
    footer_home()
