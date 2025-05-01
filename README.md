# 🎧 Podcast Summariser

A Flask web app where users can enter a podcast RSS URL, view the latest 10 episodes, select up to 3 for summarisation, and receive AI-generated summaries via email in `.docx` format.

---

## 🚀 Features

- Input a podcast RSS feed URL
- Automatically fetch and display the 10 latest episodes
- Users can select up to 3 episodes for summarisation
- Summaries are generated using AI (e.g. OpenAI API)
- Email delivery of summaries as Word (.docx) documents

---

## 🗂️ Project Structure

```
podcast_summariser/
├── app.py              # Main Flask application entry point
├── config.py           # Stores API tokens and configuration variables
├── templates/          # Jinja2 HTML templates
│   ├── base.html       # Base layout for pages
│   ├── index.html      # Input form and episode selection
│   └── subscribe.html  # Email submission confirmation
└── static/css/         # (Optional) Custom CSS styles
```

---

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/podcast_summariser.git
cd podcast_summariser
```

2. **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure `config.py`**

Example:

```python
# config.py
OPENAI_API_KEY = "your-api-key-here"
MAIL_SERVER = "smtp.yourmail.com"
MAIL_USERNAME = "your-email"
MAIL_PASSWORD = "your-email-password"
```

5. **Run the app**

```bash
python app.py
```

Then visit: `http://localhost:5000`

---

## 📦 Key Dependencies

- Flask
- Requests
- feedparser (for reading podcast RSS feeds)
- OpenAI or similar AI summarisation API
- python-docx (for generating Word documents)
- Flask-Mail (for sending summaries by email)

---

## 📬 Workflow

1. User enters podcast RSS feed URL.
2. App parses feed and displays 10 most recent episodes.
3. User selects up to 3 episodes.
4. Summaries are generated via API and converted to `.docx`.
5. `.docx` files are emailed to the user.

---

## 🧾 License

MIT License. See `LICENSE` for details.
