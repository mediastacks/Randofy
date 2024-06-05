import os
import random
import time
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException

# Load credentials from .env file
load_dotenv()
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
USERNAME = os.getenv('SPOTIPY_USERNAME')

# Authentication
scope = "user-library-read user-read-playback-state user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope, username=USERNAME))

def get_random_track(sp):
    try:
        # Fetch a list of categories
        categories = sp.categories(limit=50)['categories']['items']
        category = random.choice(categories)['id']
        
        # Fetch a random playlist from the chosen category
        playlists = sp.category_playlists(category_id=category, limit=50)['playlists']['items']
        playlist = random.choice(playlists)['id']
        
        # Fetch the tracks from the chosen playlist
        tracks = sp.playlist_tracks(playlist, limit=100)['items']
        track = random.choice(tracks)['track']
        
        return track
    except SpotifyException as e:
        if e.http_status == 429:
            # Handle rate limiting
            retry_after = int(e.headers.get('Retry-After', 1))
            print(f"Rate limited. Retrying after {retry_after} seconds.")
            time.sleep(retry_after)
            return get_random_track(sp)
        else:
            raise

def play_track(sp, track_uri):
    devices = sp.devices()
    if devices['devices']:
        device_id = devices['devices'][0]['id']
        sp.start_playback(device_id=device_id, uris=[track_uri])
    else:
        print("No active devices found.")

if __name__ == "__main__":
    track = get_random_track(sp)
    print(f"Playing: {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")
    play_track(sp, track['uri'])