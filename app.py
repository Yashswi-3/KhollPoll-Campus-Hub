import streamlit as st
from app_pages import home, mess_reviews, events, news
from components.auth import simple_auth
from components.ui import load_css, render_header

# Page config
st.set_page_config(
    page_title="KhollPoll",
    page_icon=r"assets\img\logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Load CSS
    load_css()
    
    # Simple authentication
    if not simple_auth():
        return
    
    # Header
    render_header()
    
    # Clear any existing sidebar content
    st.sidebar.empty()
    
    # Single navigation menu
    with st.sidebar:
        st.markdown("### 🧭 Navigate")
        
        # Initialize page state
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'home'
        
        # Navigation buttons with unique keys
        if st.button("🏠 Home", key="nav_home", use_container_width=True):
            st.session_state.current_page = 'home'
            st.rerun()
        
        if st.button("🍽️ Mess Reviews", key="nav_mess", use_container_width=True):
            st.session_state.current_page = 'mess'
            st.rerun()
        
        if st.button("🎉 Events", key="nav_events", use_container_width=True):
            st.session_state.current_page = 'events'
            st.rerun()
        
        if st.button("📰 News", key="nav_news", use_container_width=True):
            st.session_state.current_page = 'news'
            st.rerun()
        
        # Show current user
        st.sidebar.divider()
        st.sidebar.write(f"👤 **User:** {st.session_state.get('username', 'Unknown')}")
        
        # Logout button
        if st.sidebar.button("🚪 Logout", key="logout_btn"):
            st.session_state.authenticated = False
            st.session_state.current_page = 'home'
            st.rerun()
    
    # Route to pages based on current_page
    current_page = st.session_state.get('current_page', 'home')
    
    if current_page == 'home':
        home.show()
    elif current_page == 'mess':
        mess_reviews.show()
    elif current_page == 'events':
        events.show()
    elif current_page == 'news':
        news.show()
    else:
        home.show()  # Default fallback

if __name__ == "__main__":
    main()
