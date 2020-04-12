import os

import tweepy
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
auth.set_access_token(os.getenv("TOKEN"), os.getenv("TOKEN_SECRET"))

API = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

app = Flask(__name__)
CORS(app)

# http://docs.tweepy.org/en/latest/api.html#API.search_users
@app.route('/api/1.0/profiles/<string:query>/<int:per_page>/<int:page>', methods=['GET'])
def get_profiles(query='Test', per_page=20, page=1):
    try:
        profiles = API.search_users(query, per_page, page)
        return jsonify(profiles)
    except tweepy.TweepError:
        print('Ouch! I have to capture this')


# http://docs.tweepy.org/en/latest/api.html#API.create_block
@app.route('/api/1.0/profiles/block/<int:user_id>', methods=['POST'])
def block_user(user_id='Test'):
    try:
        response = API.create_block(user_id)
        return jsonify(response)
    except tweepy.TweepError:
        print('Ouch! I have to capture this')

# http://docs.tweepy.org/en/latest/api.html#API.search
@app.route('/api/1.0/search/<string:query>', methods=['GET'])
def get_results(query='Test'):
    try:
        results = API.search(q=query, geocode='40.416775,-3.703790,1000km', lang='es')
        return jsonify(results)
    except tweepy.TweepError:
        print('Ouch! I have to capture this')
