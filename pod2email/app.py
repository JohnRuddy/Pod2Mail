from flask import Flask, render_template, request, send_file
import requests
import xml.etree.ElementTree as ET
from config import Config
import openai
from docx import Document
import os

app = Flask(__name__)
app.config.from_object(Config)

# Set OpenAI API key
openai.api_key = app.config["OPENAI_API_KEY"]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/load_podcast", methods=["GET", "POST"])
def load_podcast():
    episodes = []
    if request.method == "POST":
        rss_url = request.form.get("rss_url")
        try:
            response = requests.get(rss_url)
            response.raise_for_status()  # Raise an error for bad responses
            root = ET.fromstring(response.content)

            # Parse the RSS feed
            for item in root.findall(".//item")[:10]:  # Get up to 10 episodes
                title = item.find("title").text if item.find("title") is not None else "No Title"
                link = item.find("link").text if item.find("link") is not None else "No Link"
                pub_date = item.find("pubDate").text if item.find("pubDate") is not None else "Unknown"
                enclosure = item.find("enclosure")
                audio_url = enclosure.get("url") if enclosure is not None else None
                episodes.append({
                    "id": link,
                    "title": title,
                    "published_date": pub_date,
                    "audio_url": audio_url,
                })
        except Exception as e:
            print(f"Error fetching or parsing RSS feed: {e}")
    return render_template("load_podcast.html", episodes=episodes)

@app.route("/summarize", methods=["POST"])
def summarize():
    selected_episodes = request.form.getlist("selected_episodes")
    episodes = request.form.to_dict(flat=False)  # Get all form data as a dictionary
    summaries = []

    for episode_id in selected_episodes:
        # Find the episode's audio URL
        audio_url = None
        for i in range(len(episodes.get("episodes[0][id]", []))):
            if episodes[f"episodes[{i}][id]"][0] == episode_id:
                audio_url = episodes[f"episodes[{i}][audio_url]"][0]
                break

        if audio_url:
            try:
                # Use OpenAI API to transcribe the audio
                audio_content = requests.get(audio_url).content
                transcription_response = openai.Audio.transcribe("whisper-1", audio_content)
                transcription_text = transcription_response["text"]

                # Use OpenAI API to summarize the transcription
                summary_response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Summarize the following text into bullet points:\n\n{transcription_text}",
                    max_tokens=150,
                    temperature=0.7,
                )
                summary_text = summary_response["choices"][0]["text"]

                # Save the summary to a Word document
                doc = Document()
                doc.add_heading(f"Summary for Episode {episode_id}", level=1)
                for bullet in summary_text.split("\n"):
                    if bullet.strip():
                        doc.add_paragraph(bullet.strip(), style="List Bullet")
                file_path = f"summary_{episode_id}.docx"
                doc.save(file_path)

                summaries.append({
                    "episode_id": episode_id,
                    "file_path": file_path,
                })
            except Exception as e:
                print(f"Error processing episode {episode_id}: {e}")

    return render_template("summarize.html", summaries=summaries)

@app.route("/download/<path:filename>")
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
