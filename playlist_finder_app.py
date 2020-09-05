from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from SpotifyAPI import SpotifyAPI
import pprint
from config import *

pp = pprint.PrettyPrinter(indent=2)

SPOTIFY_CLIENT_ID = SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET = SPOTIFY_CLIENT_SECRET

app = Flask(__name__)

spotify = SpotifyAPI(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)

@app.route('/form', methods=['POST'])
def form():
    # get user entered key words from form
    entered_text = request.form['keywords-single-str']
    keywords_list = entered_text.split(',')

    # do spotify search from keywords
    spotify.auth()
    playlists = spotify.find_playlists(keywords_list)['playlists']['items']
    # update UI with the playlist info
    return render_template('form.html', playlists=playlists)

@app.route('/')
def home():
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)