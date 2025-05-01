from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import MAILCHIMP_API_KEY, MAILCHIMP_SERVER_PREFIX
import os
import redis
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///podcasts.db'
db = SQLAlchemy(app)

# Redis setup
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80))

class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    rss_url = db.Column(db.String(500), unique=True)
    mailchimp_list_id = db.Column(db.String(100))

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcast.id'))

# Routes
@app.route('/')
def index():
    podcasts = Podcast.query.all()
    return render_template('index.html', podcasts=podcasts)

@app.route('/add-podcast', methods=['GET', 'POST'])
def add_podcast():
    if request.method == 'POST':
        title = request.form['title']
        rss_url = request.form['rss_url']

        # Save podcast data to Redis as a JSON document
        podcast_data = {
            'title': title,
            'rss_url': rss_url
        }
        redis_client.set(f'podcast:{title}', json.dumps(podcast_data))

        flash('Podcast added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add-podcast.html')

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        rss_url = request.form['rss_url']

        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email, name=name)
            db.session.add(user)
            db.session.commit()

        podcast = Podcast.query.filter_by(rss_url=rss_url).first()
        if not podcast:
            podcast = Podcast(title=rss_url, rss_url=rss_url, mailchimp_list_id='placeholder-id')
            db.session.add(podcast)
            db.session.commit()

        subscription = Subscription.query.filter_by(user_id=user.id, podcast_id=podcast.id).first()
        if not subscription:
            subscription = Subscription(user_id=user.id, podcast_id=podcast.id)
            db.session.add(subscription)
            db.session.commit()

        flash('Subscribed successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('subscribe.html')

if __name__ == '__main__':
    if not os.path.exists('podcasts.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
