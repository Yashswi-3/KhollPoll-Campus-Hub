import streamlit as st
import base64

def load_css():
    """Load custom CSS with proper color contrast"""
    st.markdown("""
    <style>
    .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: var(--text-color) !important;
    }
    
    .event-card {
        background: var(--background-color) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--secondary-background-color) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
    }

    .main-header img {
        height: 50px;
        width: 50px;
        margin-right: 10px;
        vertical-align: middle;
    }

    .event-card h3, .event-card p {
        color: var(--text-color) !important;
    }
    </style>
    """, unsafe_allow_html=True)

def image_to_base64(img_path):
    """Convert local image to base64"""
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def render_header():
    """Render main header with image logo"""
    logo_base64 = image_to_base64("assets/img/logo.png")
    st.markdown(f"""
    <div class="main-header">
        <h1>
            <img src="data:image/png;base64,{logo_base64}"/>
            KhollPoll
        </h1>
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

# Example usage
if __name__ == "__main__":
    load_css()
    render_header()
    metric_card("Events", "15")
