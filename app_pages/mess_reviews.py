import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_manager import SimpleDataManager
from components.ui import metric_card

def show():
    """Show mess reviews page"""
    st.title("🍽️ Mess Reviews")
    
    dm = SimpleDataManager()
    
    # Tabs
    tab1, tab2 = st.tabs(["📊 Dashboard", "⭐ Rate Today"])
    
    with tab1:
        show_dashboard(dm)
    
    with tab2:
        show_rating_form(dm)

def show_dashboard(dm):
    """Show reviews dashboard"""
    reviews = dm.get_reviews()
    
    if not reviews:
        st.info("No reviews yet. Be the first to rate!")
        return
    
    # Convert to DataFrame
    df = pd.DataFrame(reviews)
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        metric_card("Total Reviews", len(reviews), "📝")
    with col2:
        avg_rating = df['overall'].mean() if 'overall' in df.columns else 0
        metric_card("Avg Rating", f"{avg_rating:.1f}⭐", "📊")
    with col3:
        metric_card("This Week", len([r for r in reviews[-7:]]), "📅")
    with col4:
        metric_card("Active Users", len(set(r.get('user', '') for r in reviews)), "👥")
    
    # Chart
    if len(reviews) > 1:
        fig = px.line(df, x='timestamp', y='overall', 
                     title="Rating Trends Over Time")
        st.plotly_chart(fig, use_container_width=True)

def show_rating_form(dm):
    """Show rating form"""
    st.subheader("Rate Today's Meals")
    
    with st.form("rating_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            breakfast = st.slider("🌅 Breakfast", 1, 5, 4)
            lunch = st.slider("☀️ Lunch", 1, 5, 4)
        
        with col2:
            snacks = st.slider("🍪 Snacks", 1, 5, 4)
            dinner = st.slider("🌙 Dinner", 1, 5, 4)
        
        comments = st.text_area("💬 Comments")
        
        if st.form_submit_button("Submit Review", type="primary"):
            overall = (breakfast + lunch + snacks + dinner) / 4
            
            review = {
                'user': st.session_state.get('username', 'Anonymous'),
                'breakfast': breakfast,
                'lunch': lunch,
                'snacks': snacks,
                'dinner': dinner,
                'overall': overall,
                'comments': comments
            }
            
            dm.add_review(review)
            st.success("✅ Review submitted!")
            st.balloons()
