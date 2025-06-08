import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional

class SimpleDataManager:
    """Simple JSON-based data manager for KhollPoll"""
    
    def __init__(self, file_path: str = "data/reviews.json"):
        self.file_path = file_path
        self.ensure_data_file()
    
    def ensure_data_file(self):
        """Create data file and directory if they don't exist"""
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        
        # Create file with initial structure if it doesn't exist
        if not os.path.exists(self.file_path):
            initial_data = {
                "reviews": [],
                "events": [],
                "news": [],
                "users": [
                    {"username": "admin", "password": "password123", "role": "admin"},
                    {"username": "E22CSEU1156", "password": "student123", "role": "student"}
                ]
            }
            self.save_data(initial_data)

    
    def load_data(self) -> Dict[str, List]:
        """Load data from JSON file"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Ensure all required keys exist
            if 'reviews' not in data:
                data['reviews'] = []
            if 'events' not in data:
                data['events'] = []
            if 'news' not in data:
                data['news'] = []
                
            return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
            # Return default structure
            return {
                "reviews": [],
                "events": [],
                "news": []
            }
    
    def save_data(self, data: Dict[str, Any]) -> bool:
        """Save data to JSON file"""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
        
    def get_users(self):
        data = self.load_data()
        return data.get('users', [])

    def add_user(self, username, password, role="student"):
        data = self.load_data()
        if 'users' not in data:
            data['users'] = []
        if any(u['username'] == username for u in data['users']):
            return False
        data['users'].append({
            "username": username,
            "password": password,
            "role": role
        })
        self.save_data(data)
        return True

    def validate_user(self, username, password):
        users = self.get_users()
        for user in users:
            if user['username'] == username and user['password'] == password:
                return user
        return None
    
    def add_review(self, review_data: Dict[str, Any]) -> bool:
        """Add a new review"""
        try:
            data = self.load_data()
            
            # Add timestamp if not present
            if 'timestamp' not in review_data:
                review_data['timestamp'] = datetime.now().isoformat()
            
            # Calculate overall rating if not present
            if 'overall' not in review_data:
                ratings = []
                for meal in ['breakfast', 'lunch', 'snacks', 'dinner']:
                    if meal in review_data and review_data[meal] is not None:
                        ratings.append(review_data[meal])
                
                if ratings:
                    review_data['overall'] = sum(ratings) / len(ratings)
                else:
                    review_data['overall'] = 0
            
            data['reviews'].append(review_data)
            return self.save_data(data)
            
        except Exception as e:
            print(f"Error adding review: {e}")
            return False
    
    def get_reviews(self, limit: Optional[int] = None) -> List[Dict]:
        """Get all reviews or limited number"""
        try:
            data = self.load_data()
            reviews = data.get('reviews', [])
            
            if limit:
                return reviews[-limit:]  # Get last N reviews
            return reviews
            
        except Exception as e:
            print(f"Error getting reviews: {e}")
            return []
    
    def add_event(self, event_data):
        """Add a new event"""
        try:
            data = self.load_data()
            
            # Add creation timestamp if not present
            if 'created_at' not in event_data:
                event_data['created_at'] = datetime.now().isoformat()
            
            # Ensure events list exists
            if 'events' not in data:
                data['events'] = []
            
            data['events'].append(event_data)
            return self.save_data(data)
            
        except Exception as e:
            print(f"Error adding event: {e}")
            return False

    
    def get_events(self) -> List[Dict]:
        """Get all events"""
        try:
            data = self.load_data()
            return data.get('events', [])
        except Exception as e:
            print(f"Error getting events: {e}")
            return []
    
    def add_news(self, news_data: Dict[str, Any]) -> bool:
        """Add a new news article"""
        try:
            data = self.load_data()
            
            # Add creation timestamp
            if 'created_at' not in news_data:
                news_data['created_at'] = datetime.now().isoformat()
            
            # Add date if not present
            if 'date' not in news_data:
                news_data['date'] = datetime.now().strftime('%Y-%m-%d')
            
            data['news'].append(news_data)
            return self.save_data(data)
            
        except Exception as e:
            print(f"Error adding news: {e}")
            return False
    
    def get_news(self) -> List[Dict]:
        """Get all news articles"""
        try:
            data = self.load_data()
            return data.get('news', [])
        except Exception as e:
            print(f"Error getting news: {e}")
            return []
    
    def has_rated_today(self, user_id: str) -> bool:
        """Check if user has already rated today"""
        try:
            reviews = self.get_reviews()
            today = datetime.now().strftime('%Y-%m-%d')
            
            for review in reviews:
                review_date = review.get('timestamp', '')[:10]  # Get date part
                if review.get('user') == user_id and review_date == today:
                    return True
            
            return False
            
        except Exception as e:
            print(f"Error checking daily rating: {e}")
            return False
    
    def get_average_ratings(self, days: int = 7) -> Dict[str, float]:
        """Get average ratings for the last N days"""
        try:
            reviews = self.get_reviews()
            
            if not reviews:
                return {
                    'breakfast': 0,
                    'lunch': 0,
                    'snacks': 0,
                    'dinner': 0,
                    'overall': 0
                }
            
            # Filter reviews from last N days
            cutoff_date = datetime.now() - timedelta(days=days)
            recent_reviews = []
            
            for review in reviews:
                try:
                    review_date = datetime.fromisoformat(review.get('timestamp', ''))
                    if review_date >= cutoff_date:
                        recent_reviews.append(review)
                except:
                    continue
            
            if not recent_reviews:
                return {
                    'breakfast': 0,
                    'lunch': 0,
                    'snacks': 0,
                    'dinner': 0,
                    'overall': 0
                }
            
            # Calculate averages
            averages = {}
            for meal in ['breakfast', 'lunch', 'snacks', 'dinner', 'overall']:
                ratings = [r.get(meal, 0) for r in recent_reviews if r.get(meal) is not None]
                averages[meal] = sum(ratings) / len(ratings) if ratings else 0
            
            return averages
            
        except Exception as e:
            print(f"Error calculating averages: {e}")
            return {
                'breakfast': 0,
                'lunch': 0,
                'snacks': 0,
                'dinner': 0,
                'overall': 0
            }
    
    def get_stats(self) -> Dict[str, Any]:
        """Get general statistics"""
        try:
            data = self.load_data()
            
            reviews = data.get('reviews', [])
            events = data.get('events', [])
            news = data.get('news', [])
            
            # Get unique users
            unique_users = set()
            for review in reviews:
                if review.get('user'):
                    unique_users.add(review.get('user'))
            
            # Get recent reviews (last 7 days)
            recent_reviews = []
            cutoff_date = datetime.now() - timedelta(days=7)
            
            for review in reviews:
                try:
                    review_date = datetime.fromisoformat(review.get('timestamp', ''))
                    if review_date >= cutoff_date:
                        recent_reviews.append(review)
                except:
                    continue
            
            return {
                'total_reviews': len(reviews),
                'total_events': len(events),
                'total_news': len(news),
                'active_users': len(unique_users),
                'recent_reviews': len(recent_reviews),
                'avg_rating': sum(r.get('overall', 0) for r in reviews) / len(reviews) if reviews else 0
            }
            
        except Exception as e:
            print(f"Error getting stats: {e}")
            return {
                'total_reviews': 0,
                'total_events': 0,
                'total_news': 0,
                'active_users': 0,
                'recent_reviews': 0,
                'avg_rating': 0
            }
        
    
        


# Add missing import for timedelta
from datetime import timedelta
