import streamlit as st

def load_css():
    """Load custom CSS with proper color contrast"""
    st.markdown("""
    <style>
    /* Force text colors for better visibility */
    .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: var(--text-color) !important;
    }
    
    /* Event card styling with proper contrast */
    .event-card {
        background: var(--background-color) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--secondary-background-color) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
    }
    
    .event-card h3 {
        color: var(--text-color) !important;
    }
    
    .event-card p {
        color: var(--text-color) !important;
    }
    </style>
    """, unsafe_allow_html=True)


def render_header():
    """Render main header"""
    st.markdown("""
    <div class="main-header">
        <h1>🎓 KhollPoll - Campus Hub</h1>
        <p>Where Campus Voices Meet Action</p>
    </div>
    """, unsafe_allow_html=True)

def metric_card(title, value, icon="📊"):
    """Simple metric card component"""
    st.markdown(f"""
    <div class="metric-card">
        <h3>{icon} {title}</h3>
        <h2>{value}</h2>
    </div>
    """, unsafe_allow_html=True)
