import streamlit as st
from datetime import datetime, timedelta
import json

def format_date(date_string):
    """Format date string for display"""
    try:
        date_obj = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return date_obj.strftime('%B %d, %Y')
    except:
        return date_string

def calculate_days_ago(date_string):
    """Calculate how many days ago a date was"""
    try:
        date_obj = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        days_diff = (datetime.now() - date_obj).days
        
        if days_diff == 0:
            return "Today"
        elif days_diff == 1:
            return "Yesterday"
        else:
            return f"{days_diff} days ago"
    except:
        return "Unknown"

def validate_rating(rating):
    """Validate rating is between 1 and 5"""
    try:
        rating = float(rating)
        return 1 <= rating <= 5
    except:
        return False

def get_rating_emoji(rating):
    """Get emoji based on rating"""
    if rating >= 4.5:
        return "🌟"
    elif rating >= 4.0:
        return "⭐"
    elif rating >= 3.0:
        return "👍"
    elif rating >= 2.0:
        return "👎"
    else:
        return "😞"

def truncate_text(text, max_length=100):
    """Truncate text to specified length"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def is_admin_user(username):
    """Check if user is admin"""
    admin_users = ['admin', 'E22CSEU1156']
    return username in admin_users

def generate_sample_data():
    """Generate sample data for testing"""
    return {
        "reviews": [
            {
                "user": "E22CSEU1156",
                "breakfast": 4,
                "lunch": 5,
                "snacks": 3,
                "dinner": 4,
                "overall": 4.0,
                "comments": "Good food today!",
                "timestamp": "2024-05-20T12:00:00"
            }
        ],
        "events": [],
        "news": []
    }

def safe_get(dictionary, key, default=None):
    """Safely get value from dictionary"""
    try:
        return dictionary.get(key, default)
    except:
        return default

def format_timestamp(timestamp):
    """Format timestamp for display"""
    try:
        dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M')
    except:
        return timestamp
