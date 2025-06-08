import streamlit as st
from datetime import datetime
from utils.data_manager import SimpleDataManager
from PIL import Image
import os

def show():
    """Show events page"""
    st.title("🎉 Campus Events")

    dm = SimpleDataManager()

    tab1, tab2 = st.tabs(["📅 Upcoming Events", "➕ Add Event"])

    with tab1:
        show_events(dm)

    with tab2:
        add_event_form(dm)

def show_events(dm):
    """Display events with poster-image layout and all previous functionality"""
    try:
        data = dm.load_data()
        events = data.get('events', [])

        # If no events exist, add sample events
        if not events:
            st.info("No events found. Adding sample events...")
            events = get_sample_events()
            data['events'] = events
            dm.save_data(data)
            st.success("Sample events added!")

        # Search and filter section
        st.subheader("🔍 Find Events")
        col1, col2 = st.columns([3, 1])
        with col1:
            search = st.text_input("Search events...", placeholder="Search by title, organizer, or description")
        with col2:
            category = st.selectbox("Category", ["All", "Academic", "Cultural", "Sports", "Technical"])

        # Filter events
        filtered_events = events
        if search:
            search_lower = search.lower()
            filtered_events = [
                e for e in filtered_events
                if (search_lower in e.get('title', '').lower() or
                    search_lower in e.get('organizer', '').lower() or
                    search_lower in e.get('description', '').lower())
            ]
        if category != "All":
            filtered_events = [e for e in filtered_events if e.get('category') == category]

        # Display results count
        if not filtered_events:
            st.warning("❌ No events found matching your criteria.")
            st.info("💡 Try adjusting your search terms or category filter.")
            return

        st.success(f"✅ Found {len(filtered_events)} event(s)")
        st.write("---")

        # Display each event with poster-image layout
        for event in filtered_events:
            st.markdown(f"#### {event.get('organizer', 'Organizer')} PRESENTS")
            col1, col2, col3 = st.columns([2, 3, 1])

            # Poster (left)
            with col1:
                poster_path = event.get('poster', 'assets/default.jpg')
                if os.path.exists(poster_path):
                    try:
                        img = Image.open(poster_path)
                        img = img.resize((450, 300))  # Fixed size (width, height)
                        st.image(img)
                    except Exception:
                        st.info("Could not open image.")
                else:
                    st.info("No poster available.")

            # Event details (center)
            with col2:
                st.markdown(f"**{event.get('title', 'Untitled Event')}**")
                st.write(event.get('description', 'No description available.'))
                if event.get('link'):
                    st.markdown(f"[Site LINK...]({event['link']})")

            # Date & Venue (right)
            with col3:
                st.markdown(f"**Date & Venue**\n\n{event.get('date', 'TBD')}\n\n{event.get('venue', 'TBD')}")

            st.markdown("---")

    except Exception as e:
        st.error(f"❌ Error loading events: {str(e)}")
        st.info("🔄 Please try refreshing the page.")
        with st.expander("🐛 Debug Information"):
            st.write(f"Error details: {e}")

def add_event_form(dm):
    """Form to add new events, including poster path"""
    st.subheader("➕ Add New Event")

    # Check if user is admin
    username = st.session_state.get('username', '')
    if username not in ['admin', 'E22CSEU1156']:
        st.warning("⚠️ Only admins can add events.")
        st.info("Please contact an administrator to add events.")
        return

    

def get_sample_events():
    return [
        {
            'organizer': 'WIE',
            'poster': 'assets/img/l5.png',
            'title': 'FILS',
            'description': 'WIE is coming with FILS for freelancing, internship, linkedin and startup. Get to know about the important topics.',
            'link': 'https://example.com/fils',
            'date': '2024-06-11',
            'venue': 'NLH-103',
            'category': 'Technical'
        },
        {
            'organizer': 'GFG',
            'poster': 'assets/img/s1.png',
            'title': 'SPIN THE CODE',
            'description': 'GFG presents SPIN the Code...',
            'link': 'https://example.com/spin_code',
            'date': '2024-06-01',
            'venue': 'ALH-002',
            'category': 'Technical'
        },
        {
            'organizer': 'ATC',
            'poster': 'assets/img/s3.png',
            'title': 'BULLETPROOF',
            'description': "Alan Turing Club: ...",
            'link': 'https://example.com/bulletproof',
            'date': '2024-05-28',
            'venue': 'ALH-002',
            'category': 'Academic'
        }
    ]
