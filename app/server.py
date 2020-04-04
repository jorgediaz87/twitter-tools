import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
import tweepy

auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
auth.set_access_token(os.getenv("TOKEN"), os.getenv("TOKEN_SECRET"))

API = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/1.0/profiles/<string:query>', methods=['GET'])
def get_profiles(query='Test'):
    profiles = API.search_users(query)
    return jsonify(profiles)


@app.route('/api/1.0/profiles/block/<int:user_id>', methods=['POST'])
def block_user(user_id='Test'):
    try:
        response = API.create_block(user_id)
        return jsonify(response)
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
