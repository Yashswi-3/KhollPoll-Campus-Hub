import streamlit as st
from utils.data_manager import SimpleDataManager

def simple_auth():
    dm = SimpleDataManager()
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'show_signup' not in st.session_state:
        st.session_state.show_signup = False

    if st.session_state.show_signup:
        signup_form(dm)
        return False

    if not st.session_state.authenticated:
        st.title("🔐 Login to KhollPoll")
        with st.form("login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            if submit:
                user = dm.validate_user(username, password)
                if user:
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.session_state.role = user.get('role', 'student')
                    st.success("✅ Login successful!")
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials")
        st.info("Don't have an account?")
        if st.button("Sign Up"):
            st.session_state.show_signup = True
        return False
    return True

def signup_form(dm):
    st.title("📝 Sign Up for KhollPoll")
    with st.form("signup"):
        username = st.text_input("Choose a Username")
        password = st.text_input("Choose a Password", type="password")
        confirm = st.text_input("Confirm Password", type="password")
        submit = st.form_submit_button("Sign Up")
        if submit:
            if not username or not password:
                st.error("Please fill all fields.")
            elif password != confirm:
                st.error("Passwords do not match.")
            elif dm.add_user(username, password):
                st.success("Account created! Please log in.")
                st.session_state.show_signup = False
            else:
                st.error("Username already exists.")
    if st.button("Back to Login"):
        st.session_state.show_signup = False
