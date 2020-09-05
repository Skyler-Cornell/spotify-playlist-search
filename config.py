"""
Necessary spotify development credentials should be stored in an environemnt variable
on your trusted machine. The credentials SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET are 
stored as environment variables on the Heroku servers (heroku app settings) and locally
on my development computer
"""
import os

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
if not SPOTIFY_CLIENT_ID:
    raise RuntimeError("Required environment variable SPOTIFY_CLIENT_ID is not defined")

SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
if not SPOTIFY_CLIENT_SECRET:
    raise RuntimeError("Required environment variable SPOTIFY_CLIENT_SECRET is not defined")
