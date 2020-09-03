from flask import Flask, request, render_template
from SpotifyAPI import SpotifyAPI
#pp = pprint.PrettyPrinter(indent=2)
CLIENT_ID = '9008c46566394946badacf432c783c08'
CLIENT_SECRET = '85c80468c4234b0bb05db88ea53aed0c'


app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')


#sp_client = SpotifyAPI(client_id=CLIENT_ID,client_secret=CLIENT_SECRET)
# authenticate and set access_token within object
#sp_client.auth()

#matching_playlists = sp_client.find_playlists(keywords=['indie','rock'])['playlists']['items']

#pp.pprint(matching_playlists)


if __name__ == "__main__":
    app.run(debug=True)