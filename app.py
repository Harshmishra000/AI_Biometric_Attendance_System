import streamlit as st

def safe_import():
    try:
        from screens.home_screen import home_screen
        from screens.teacher_screen import teacher_screen
        from screens.student_screen import student_screen
        from components.dialog_auto_enroll import auto_enroll_dialog
        return home_screen, teacher_screen, student_screen, auto_enroll_dialog
    except Exception as e:
        st.error(f"Import Error: {e}")
        return None, None, None, None


home_screen, teacher_screen, student_screen, auto_enroll_dialog = safe_import()

def main():
    st.set_page_config(
        page_title='smartAttendance - AI Attendance System',
        page_icon="📊"
    )

    if home_screen is None:
        st.stop()

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    if st.session_state['login_type'] == 'teacher':
        teacher_screen()

    elif st.session_state['login_type'] == 'student':
        student_screen()

    else:
        home_screen()

    join_code = st.query_params.get('join-code')

    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()

        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)

if __name__ == "__main__":
    main()
