import requests
import base64
import json
import pprint
from urllib.parse import urlencode

pp = pprint.PrettyPrinter(indent=2)
CLIENT_ID = '9008c46566394946badacf432c783c08'
CLIENT_SECRET = '85c80468c4234b0bb05db88ea53aed0c'


class SpotifyAPI(object):
    """
    For interfacing with Spotify API
    """
    token_url = 'https://accounts.spotify.com/api/token'
    access_token = None
    token_data = None
    token_headers = None

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Returns base 64 encoded client credientials
        """
        client_creds_byte = (self.client_id+':'+self.client_secret).encode()
        client_creds_b64 = str(base64.b64encode(client_creds_byte).decode())
        return client_creds_b64

    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        authorization_b64 = 'Basic ' + client_creds_b64
        token_headers = {
            'Authorization':authorization_b64
        }
        return token_headers

    def get_token_data(self):
        token_data = {
            'grant_type':'client_credentials',
        }
        return token_data

    def auth(self):

        req = requests.post(self.token_url, data=self.get_token_data(), headers=self.get_token_headers())

        if not req.ok:
            return False

        access_token = req.json()['access_token']
        self.access_token = access_token
        return True


    def find_playlists(self, playlist_keywords):
        """
        Returns a list of popular public playlists that match the
        keywords query.
        """
        query = playlist_keywords
        endpoint_url = 'https://api.spotify.com/v1/search'

        headers = {
            'Authorization': 'Bearer ' + str(self.access_token)
        }
        request_data = {
            'q':query,
            'type':'playlist'
        }

        search_url = endpoint_url + '?' +urlencode(request_data)

        req = requests.get(search_url, headers=headers)

        if not req.ok:
            return req.status_code

        return req.json()

sp_client = SpotifyAPI(client_id=CLIENT_ID,client_secret=CLIENT_SECRET)
# authenticate and set access_token within object
sp_client.auth()

playlist_data = sp_client.find_playlists(playlist_keywords='skating')['playlists']['items'][0]

pp.pprint(playlist_data)