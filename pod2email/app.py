from flask import Flask, render_template, request
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

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
                episodes.append({
                    "id": link,
                    "title": title,
                    "published_date": pub_date,
                })
        except Exception as e:
            print(f"Error fetching or parsing RSS feed: {e}")
    return render_template("load_podcast.html", episodes=episodes)

@app.route("/summarize", methods=["POST"])
def summarize():
    selected_episodes = request.form.getlist("selected_episodes")
    # Logic for summarizing the selected episodes goes here
    return f"Summarizing episodes: {', '.join(selected_episodes)}"

if __name__ == "__main__":
    app.run(debug=True)
