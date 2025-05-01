# 🎧 AI Podcast Summariser & Newsletter Service

A lightweight Flask microservice that lets users subscribe to podcast RSS feeds. For each new episode, the app transcribes the audio using AI, generates a concise summary with GPT, and sends it to all subscribers via Mailchimp.

## 🚀 Features

- 🔐 User signup with podcast URL subscription
- 🎙️ Automatic RSS feed polling for new episodes
- 🧠 AI transcription (via Whisper) and summarisation (via GPT)
- 📬 Mailchimp integration for email list management and newsletter campaigns
- 🧩 Bootstrap-styled web interface with a modular Flask backend
- 💾 SQLite for quick local development

## 📦 Tech Stack

- **Backend**: Flask, SQLAlchemy, Python
- **Frontend**: HTML5, Bootstrap 5 (via CDN)
- **AI**: OpenAI Whisper (transcription), GPT (summarisation)
- **Mailing**: Mailchimp Campaign & Audience APIs
- **Database**: SQLite

## 🛠 Folder Structure

podcast_summariser/
├── app.py # Main Flask app
├── config.py # API tokens & configuration
├── templates/ # Jinja2 HTML templates
│ ├── base.html
│ ├── index.html
│ └── subscribe.html
└── static/css/ # (Optional) Custom styles
