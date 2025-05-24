import streamlit as st
from datetime import datetime
from utils.data_manager import SimpleDataManager

def show():
    """Show news page"""
    st.title("📰 Campus News & Updates")
    
    dm = SimpleDataManager()
    
    # Tabs
    tab1, tab2 = st.tabs(["📖 Latest News", "✍️ Add News"])
    
    with tab1:
        show_news(dm)
    
    with tab2:
        add_news_form(dm)

def show_news(dm):
    """Display news articles"""
    data = dm.load_data()
    news = data.get('news', [])
    
    # Sample news if none exist
    if not news:
        news = get_sample_news()
        data['news'] = news
        dm.save_data(data)
    
    # Search functionality
    search = st.text_input("🔍 Search news...", placeholder="Search by title or content")
    
    # Filter news
    filtered_news = news
    if search:
        filtered_news = [n for n in news if search.lower() in n.get('title', '').lower() 
                        or search.lower() in n.get('content', '').lower()]
    
    if not filtered_news:
        st.info("No news articles found.")
        return
    
    # Display news
    for article in sorted(filtered_news, key=lambda x: x.get('date', ''), reverse=True):
        st.markdown(f"""
        <div class="card">
            <h3>📰 {article.get('title', 'Untitled')}</h3>
            <p><small>📅 {article.get('date', 'Unknown date')} | 🏷️ {article.get('category', 'General')}</small></p>
            <p>{article.get('content', 'No content available.')}</p>
            <p><small>✍️ By: {article.get('author', 'Unknown')}</small></p>
        </div>
        """, unsafe_allow_html=True)

def add_news_form(dm):
    """Form to add news articles"""
    st.subheader("Add News Article")
    
    # Check if user is admin
    if st.session_state.get('username') not in ['admin', 'E22CSEU1156']:
        st.warning("⚠️ Only admins can add news articles.")
        return
    
    with st.form("add_news"):
        title = st.text_input("Article Title*", placeholder="New Library Wing Opening")
        
        col1, col2 = st.columns(2)
        with col1:
            category = st.selectbox("Category*", ["Academic", "Infrastructure", "Sports", "Cultural", "General"])
        with col2:
            author = st.text_input("Author*", value=st.session_state.get('username', ''))
        
        content = st.text_area("Content*", placeholder="Write your news article here...", height=200)
        
        if st.form_submit_button("Publish Article", type="primary"):
            if title and content and author:
                article = {
                    'title': title,
                    'content': content,
                    'author': author,
                    'category': category,
                    'date': datetime.now().strftime('%Y-%m-%d'),
                    'created_at': datetime.now().isoformat()
                }
                
                data = dm.load_data()
                data['news'].append(article)
                dm.save_data(data)
                
                st.success("✅ Article published successfully!")
                st.rerun()
            else:
                st.error("❌ Please fill all required fields.")

def get_sample_news():
    """Get sample news articles"""
    return [
        {
            'title': 'New Library Wing Opening',
            'content': 'The university is opening a new modern library wing with state-of-the-art facilities including digital study pods, collaborative spaces, and an extensive collection of e-books.',
            'author': 'Admin',
            'category': 'Infrastructure',
            'date': '2024-05-20'
        },
        {
            'title': 'Summer Internship Program',
            'content': 'Applications are now open for the summer internship program with leading tech companies. Students can apply through the placement portal.',
            'author': 'Placement Cell',
            'category': 'Academic',
            'date': '2024-05-18'
        },
        {
            'title': 'Sports Week 2024',
            'content': 'Annual sports week featuring various competitions and tournaments will be held from June 1-7. Registration is open for all students.',
            'author': 'Sports Committee',
            'category': 'Sports',
            'date': '2024-05-15'
        }
    ]
