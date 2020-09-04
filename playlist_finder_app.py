from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from SpotifyAPI import SpotifyAPI
import pprint

pp = pprint.PrettyPrinter(indent=2)
CLIENT_ID = '9008c46566394946badacf432c783c08'
CLIENT_SECRET = '85c80468c4234b0bb05db88ea53aed0c'

app = Flask(__name__)

spotify = SpotifyAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

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