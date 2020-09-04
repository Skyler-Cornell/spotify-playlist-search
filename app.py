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

    # do spotify stuff with the keuwords
    spotify.auth()
    playlists = spotify.find_playlists(keywords_list)['playlists']['items']
    playlist_names = []
    playlist_owners = []
    playlist_descriptions = []

    for playlist in playlists:
        playlist_names.append(playlist['name'])
        playlist_owners.append(playlist['owner'])
        playlist_descriptions.append(playlist['description'])
    return render_template('form.html', playlist_names=playlist_names, playlist_owners=playlist_owners, playlist_descriptions=playlist_descriptions)


@app.route('/')
def home():
    return render_template('form.html')


#sp_client = SpotifyAPI(client_id=CLIENT_ID,client_secret=CLIENT_SECRET)
# authenticate and set access_token within object
#sp_client.auth()

#matching_playlists = sp_client.find_playlists(keywords=['indie','rock'])['playlists']['items']

#pp.pprint(matching_playlists)


if __name__ == "__main__":
    app.run(debug=True)