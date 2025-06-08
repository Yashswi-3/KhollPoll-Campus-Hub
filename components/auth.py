import streamlit as st
from utils.data_manager import SimpleDataManager

def simple_auth():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'show_signup' not in st.session_state:
        st.session_state.show_signup = False
    if 'show_landing' not in st.session_state:
        st.session_state.show_landing = True

    # --- LANDING PAGE ---
    if st.session_state.show_landing:
        show_landing_page()
        return False

    # --- SIGNUP PAGE ---
    if st.session_state.show_signup:
        signup_form(SimpleDataManager())
        return False

    # --- LOGIN PAGE ---
    if not st.session_state.authenticated:
        login_form(SimpleDataManager())
        return False

    return True

def show_landing_page():
    st.markdown("""
    <style>
    .landing-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        # height: 30vh;
        text-align: center;
    }
    .khollpoll-title {
        text-align: center;
        font-size: 10vw;
        font-weight: 900;
        letter-spacing: 0.05em;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 3rem;
        font-family: 'Inter', sans-serif;
        line-height: 1.1;
    }
    .button-row {
        align-items: center;
        display: flex;
        justify-content: center;
        gap: 3vw;
        margin-top: 4vh;
        width: 100%;
    }
    .stButton > button {
        width: 260px !important;
        height: 56px !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        border-radius: 28px !important;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 8px 32px rgba(102,126,234,0.22) !important;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.04) !important;
        box-shadow: 0 12px 40px rgba(102,126,234,0.33) !important;
        background: linear-gradient(90deg, #764ba2 0%, #667eea 100%) !important;
    }
    @media (max-width: 900px) {
        .khollpoll-title { font-size: 12vw; }
        .button-row { flex-direction: column; gap: 2vh; }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="landing-container">', unsafe_allow_html=True)
    st.markdown('<div class="khollpoll-title">KhollPoll</div>', unsafe_allow_html=True)
    st.markdown('<div class="button-row">', unsafe_allow_html=True)

    # Center the buttons using columns and Streamlit buttons
    col1, col2, col3 = st.columns([2,2,2], gap="large")
    with col1:
        st.empty()
    with col2:
        login = st.button("Login", key="landing_login", use_container_width=True)
        st.markdown('<div style="height: 1.5vh"></div>', unsafe_allow_html=True)
        signup = st.button("Sign Up", key="landing_signup", use_container_width=True)
    with col3:
        st.empty()

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if login:
        st.session_state.show_landing = False
        st.session_state.show_signup = False
        st.rerun()
    if signup:
        st.session_state.show_landing = False
        st.session_state.show_signup = True
        st.rerun()

def login_form(dm):
    st.markdown("""
    <style>
    .kholl-auth-box {
        max-width: 420px;
        margin: 6vh auto 0 auto;
        padding: 2.5rem 2rem 2rem 2rem;
        background: rgba(255,255,255,0.97);
        border-radius: 18px;
        box-shadow: 0 8px 32px rgba(31,38,135,0.12);
        border: 1px solid #eee;
    }
    @media (max-width: 600px) {
        .kholl-auth-box {padding: 1rem;}
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="kholl-auth-box">', unsafe_allow_html=True)
    st.title("🔒 Login to KhollPoll")
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
        st.session_state.show_landing = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def signup_form(dm):
    st.markdown("""
    <style>
    .kholl-auth-box {
        max-width: 420px;
        margin: auto auto 0 auto;
        padding: 2.5rem 2rem 2rem 2rem;
        background: rgba(255,255,255,0.97);
        border-radius: 18px;
        box-shadow: 0 8px 32px rgba(31,38,135,0.12);
        border: 1px solid #eee;
    }
    @media (max-width: 600px) {
        .kholl-auth-box {padding: 1rem;}
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="kholl-auth-box">', unsafe_allow_html=True)
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
                st.session_state.show_landing = False
                st.rerun()
            else:
                st.error("Username already exists.")
    if st.button("Back to Login"):
        st.session_state.show_signup = False
        st.session_state.show_landing = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
