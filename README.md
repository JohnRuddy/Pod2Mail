# 🎧 Podcast Summariser

A simple Flask web application that allows users to submit podcast links or audio files, and returns concise summaries using AI-driven APIs.

---

## 🚀 Features

- Submit podcast URLs or audio files
- Automatically generate summaries using AI
- Clean, responsive UI built with Jinja2 templates
- (Optional) Email subscription for updates

---

## 🗂️ Project Structure

```
podcast_summariser/
├── app.py              # Main Flask application entry point
├── config.py           # Stores API tokens and configuration variables
├── templates/          # Jinja2 HTML templates
│   ├── base.html       # Base layout for pages
│   ├── index.html      # Home page with podcast upload/form
│   └── subscribe.html  # Subscription or newsletter sign-up page
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

4. **Add your API keys to `config.py`**

Example:

```python
# config.py
OPENAI_API_KEY = "your-api-key-here"
```

5. **Run the app**

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 📦 Dependencies

- Flask
- Requests
- OpenAI API (or other summarisation services)
- (Optional) Flask-Mail or similar for subscriptions

---

## 💡 Notes

- For PDF output or advanced text extraction, consider integrating libraries like `PyMuPDF`, `pdfplumber`, or `pydub` for audio processing.
- DocuSign or similar services can be integrated for signature workflows if needed.

---

## 📬 Future Features

- Podcast transcription support
- User authentication
- Summary history & downloads
- Export summaries to PDF or email

---

## 🧾 License

MIT License. See `LICENSE` for details.
