import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def create_rating_chart(reviews_data):
    """Create rating trends chart"""
    if not reviews_data:
        return None
    
    df = pd.DataFrame(reviews_data)
    if 'timestamp' not in df.columns or 'overall' not in df.columns:
        return None
    
    # Convert timestamp to datetime
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    
    # Group by date and calculate average
    daily_avg = df.groupby('date')['overall'].mean().reset_index()
    
    fig = px.line(daily_avg, x='date', y='overall',
                  title='Daily Average Ratings',
                  labels={'overall': 'Average Rating', 'date': 'Date'})
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Inter",
        yaxis=dict(range=[1, 5])
    )
    
    return fig

def create_meal_comparison_chart(reviews_data):
    """Create meal comparison chart"""
    if not reviews_data:
        return None
    
    df = pd.DataFrame(reviews_data)
    meal_columns = ['breakfast', 'lunch', 'snacks', 'dinner']
    
    # Check if meal columns exist
    if not all(col in df.columns for col in meal_columns):
        return None
    
    # Calculate averages
    averages = df[meal_columns].mean()
    
    fig = go.Figure(data=[
        go.Bar(x=meal_columns, y=averages.values,
               marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
    ])
    
    fig.update_layout(
        title='Average Ratings by Meal',
        xaxis_title='Meal Type',
        yaxis_title='Average Rating',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Inter",
        yaxis=dict(range=[1, 5])
    )
    
    return fig

def create_rating_distribution(reviews_data):
    """Create rating distribution pie chart"""
    if not reviews_data:
        return None
    
    df = pd.DataFrame(reviews_data)
    if 'overall' not in df.columns:
        return None
    
    # Create rating bins
    df['rating_bin'] = pd.cut(df['overall'], 
                             bins=[0, 2, 3, 4, 5], 
                             labels=['Poor (1-2)', 'Fair (2-3)', 'Good (3-4)', 'Excellent (4-5)'])
    
    rating_counts = df['rating_bin'].value_counts()
    
    fig = px.pie(values=rating_counts.values, 
                names=rating_counts.index,
                title='Rating Distribution')
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_family="Inter"
    )
    
    return fig
