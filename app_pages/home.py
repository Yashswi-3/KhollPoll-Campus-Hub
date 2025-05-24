import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta
from utils.data_manager import SimpleDataManager

def show():
    """Show modern home page with enhanced design"""
    
    # Load custom CSS for this page
    load_home_css()
    
    # Main header section
    render_modern_header()
    
    # Quick action cards
    render_action_cards()
    
    # Recent activity feed
    render_activity_feed()

def load_home_css():
    """Load custom CSS for home page"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Header Styles */
    .hero-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 3rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        text-align: center;
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #6b7280;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Action Card Styles */
    .action-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: all 0.3s ease;
        text-align: center;
        cursor: pointer;
    }
    
    .action-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 40px rgba(31, 38, 135, 0.5);
    }
    
    .action-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .action-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.8rem;
    }
    
    .action-desc {
        color: #6b7280;
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    /* Stats Card Styles */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem 1.5rem;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
    }
    
    .stat-number {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .stat-label {
        font-size: 1rem;
        opacity: 0.9;
        font-weight: 500;
    }
    
    /* Activity Feed Styles */
    .activity-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .activity-item {
        background: rgba(102, 126, 234, 0.05);
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .activity-item:hover {
        background: rgba(102, 126, 234, 0.1);
        transform: translateX(5px);
    }
    
    .activity-user {
        font-weight: 600;
        color: #1f2937;
    }
    
    .activity-rating {
        color: #667eea;
        font-weight: 600;
    }
    
    .activity-time {
        color: #6b7280;
        font-size: 0.85rem;
    }
    
    .activity-comment {
        color: #4b5563;
        font-style: italic;
        margin-top: 0.5rem;
    }
    
    /* Animation Classes */
    .fade-in {
        animation: fadeIn 0.8s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .pulse-glow {
        animation: pulseGlow 3s infinite;
    }
    
    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4); }
        50% { box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6); }
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.2rem;
        }
        
        .hero-subtitle {
            font-size: 1.1rem;
        }
        
        .action-card {
            padding: 1.5rem;
        }
        
        .stat-number {
            font-size: 2.2rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def render_modern_header():
    """Render modern hero header"""
    dm = SimpleDataManager()
    stats = dm.get_stats()
    
    username = st.session_state.get('username', 'Student')
    current_time = datetime.now().strftime("%B %d, %Y")
    
    st.markdown(f"""
    <div class="hero-container fade-in">
        <h1 class="hero-title">Welcome back, {username}! 👋</h1>
        <p class="hero-subtitle">Your campus hub for reviews, events, and updates • {current_time}</p>
    </div>
    """, unsafe_allow_html=True)

def render_action_cards():
    """Render quick action cards"""
    st.markdown("## 🚀 Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="action-card fade-in">
            <span class="action-icon">🍽️</span>
            <h3 class="action-title">Rate Today's Meals</h3>
            <p class="action-desc">Share your feedback on breakfast, lunch, snacks, and dinner. Help improve our mess quality!</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🍽️ Rate Meals", key="rate_meals", use_container_width=True, type="primary"):
            st.session_state.current_page = 'mess'
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="action-card fade-in">
            <span class="action-icon">🎉</span>
            <h3 class="action-title">Discover Events</h3>
            <p class="action-desc">Explore upcoming campus events, workshops, competitions, and cultural activities.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎉 Browse Events", key="view_events", use_container_width=True, type="secondary"):
            st.session_state.current_page = 'events'
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="action-card fade-in">
            <span class="action-icon">📰</span>
            <h3 class="action-title">Campus News</h3>
            <p class="action-desc">Stay updated with the latest campus announcements, news, and important updates.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📰 Read News", key="read_news", use_container_width=True, type="secondary"):
            st.session_state.current_page = 'news'
            st.rerun()


def render_activity_feed():
    """Render recent activity feed"""
    dm = SimpleDataManager()
    recent_reviews = dm.get_reviews(limit=5)
    
    st.markdown("""
    <div class="activity-container fade-in">
        <h2 style="color: #1f2937; margin-bottom: 1.5rem;">🔥 Recent Activity</h2>
    """, unsafe_allow_html=True)
    
    if recent_reviews:
        for review in reversed(recent_reviews):
            user = review.get('user', 'Anonymous')
            rating = review.get('overall', 0)
            timestamp = review.get('timestamp', '')
            comments = review.get('comments', '')
            
            # Format timestamp
            try:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                time_str = dt.strftime('%b %d, %Y at %I:%M %p')
            except:
                time_str = timestamp[:10] if timestamp else 'Unknown time'
            
            # Determine rating emoji
            if rating >= 4.5:
                rating_emoji = "🌟"
            elif rating >= 4.0:
                rating_emoji = "⭐"
            elif rating >= 3.0:
                rating_emoji = "👍"
            else:
                rating_emoji = "👎"
            
            st.markdown(f"""
            <div class="activity-item">
                <div>
                    <span class="activity-user">{user}</span> rated today's meals 
                    <span class="activity-rating">{rating:.1f} {rating_emoji}</span>
                </div>
                <div class="activity-time">{time_str}</div>
                {f'<div class="activity-comment">"{comments}"</div>' if comments else ''}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="activity-item">
            <div style="text-align: center; color: #6b7280;">
                <span style="font-size: 2rem;">🌟</span><br>
                <strong>No recent activity</strong><br>
                Be the first to leave a review and start the conversation!
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Call-to-action if no recent activity
    if not recent_reviews:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Leave Your First Review", key="first_review", use_container_width=True, type="primary"):
                st.session_state.current_page = 'mess'
                st.rerun()
