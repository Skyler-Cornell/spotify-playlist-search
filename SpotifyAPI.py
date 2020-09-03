"""
SpotifyAPI is a class for making various Spotify API requests
"""
import requests
import base64
import json
import pprint
from urllib.parse import urlencode

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
        """
        Authenticates Spotify developer app credentials and sets self.access_token to the spotify 
        provided access token which is required in the header for most API requests
        """
        req = requests.post(self.token_url, data=self.get_token_data(), headers=self.get_token_headers())

        if not req.ok:
            return False

        access_token = req.json()['access_token']
        self.access_token = access_token
        return True

    def generate_search_query_str(self, keywords=[]):
        """
        Generates a query string

        Adds to string the contents of OR_list seperated by '%20OR%20' 
        which tells Spotify that its search results should contain any of those strings
        """
        query = ""
        # handle the ORs
        for keyword in keywords:
            query += keyword + '%20OR%20'
        return query


    def find_playlists(self, keywords=[]):
        """
        :param playlist_keywords: list of strings that the the playlist description or title should contain
                                   if playlist_keywords = ['hardcore', 'punk', 'metal'] then the playlists will limit the search
                                   such that the playlists returned contain 'hardcore' OR 'punk' OR 'metal'

        Returns a list of popular public playlists that match the query search
        """       
        search_endpoint = 'https://api.spotify.com/v1/search'

        headers = {
            'Authorization': 'Bearer ' + str(self.access_token)
        }

        query = self.generate_search_query_str(keywords=keywords)
        request_data = {
            'q':query,
            'type':'playlist'
        }
        search_url = search_endpoint + '?' +urlencode(request_data)
        req = requests.get(search_url, headers=headers)

        if not req.ok:
            return 'Something fucked up. Exit code:{}'.format(eq.status_code)

        return req.json()

