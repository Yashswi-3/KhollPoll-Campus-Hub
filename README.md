# 🎓 KhollPoll – Campus Hub

KhollPoll is a modern Streamlit web application designed for campus communities to review mess food, manage and discover events, and stay updated with campus news. It features a beautiful, responsive UI, interactive charts, and a robust admin workflow.

## 🚀 Features

🍽️ **Mess Reviews**: Rate daily meals, view trends, and see analytics.

🎉 **Campus Events**: Browse, search, and filter upcoming events. Admins can add events with posters.

📰 **News & Updates**: Stay updated with campus announcements and news.

📊 **Analytics**: Interactive charts and dashboards for mess and event data.

🖼️ **Event Posters**: Each event can display a custom poster image.

🔐 **Authentication**: Simple login system for students and admins.

🖥️ **Responsive UI**: Modern glassmorphism design, works on desktop and mobile.

🔎 **Search & Filter**: Quickly find events by keyword or category.

📝 **Admin Controls**: Only admins can add events/news.

## 📁 Project Structure

```
kholl_poll/
├── app.py                    # Main Streamlit entry point
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml           # Streamlit theme & config
├── assets/
│   └── img/                  # Event poster images
│       ├── l5.png
│       ├── s1.png
│       └── s3.png
├── components/
│   ├── ui.py                 # UI helper functions & CSS
│   └── auth.py               # Simple authentication logic
├── pages/
│   ├── __init__.py
│   ├── home.py               # Home dashboard
│   ├── mess_reviews.py       # Mess review page
│   ├── events.py             # Events page (with posters)
│   └── news.py               # News page
├── utils/
│   ├── __init__.py
│   ├── data_manager.py       # JSON data management
│   └── helpers.py            # Misc helpers
└── data/
    └── reviews.json          # Persistent data storage
```

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd kholl_poll
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add event poster images
Place your event images in the `assets/img/` directory.

Use relative paths like `assets/img/l5.png` when adding events.

### 4. Run the application
```bash
streamlit run app.py
```

### 5. Login Credentials

**Admin:**
- Username: admin
- Password: password123

**Student:**
- Username: E22CSEU1156
- Password: student123

## 🛠️ Usage

Navigate using the sidebar: Home, Mess Reviews, Events, News.

**Mess Reviews**: Rate today's meals and view analytics.

**Events**: Browse events (with posters), search/filter, or add new events (admin only).

**News**: Read campus news or add new articles (admin only).

Admins can add events/news; students can view and review.

## 🖼️ Adding Event Posters

When adding or editing an event, set the **Poster Image Path** to a relative path, e.g., `assets/img/my_poster.png`.

If no poster is provided, a default image will be used.

## 📝 Data Storage

All reviews, events, and news are stored in `data/reviews.json`.

Images are not stored in JSON; only their relative paths are.

## 🔐 Authentication

Simple username/password authentication.

Only users listed as admins can add events/news.

## 💡 Customization

**Theme**: Edit `.streamlit/config.toml` for colors and layout.

**Event Categories**: Add more categories in `events.py` if needed.

**Default Images**: Place a fallback image at `assets/default.jpg`.

## 🧩 Dependencies

- streamlit
- pandas
- Pillow (for image resizing)
- plotly (for charts)

## 📣 Credits

Developed by the KhollPoll Team  
Bennett University  
Made with ❤️ using Streamlit

## 📬 Feedback & Issues

For feedback, suggestions, or bug reports, please open an issue or contact the project maintainers.

Enjoy your new campus hub! 🚀

**Tip:**
If you ever see "No poster available," check your image path and make sure the file exists in `assets/img/`.

Let me know if you want to add badges, screenshots, or a section for deployment instructions!