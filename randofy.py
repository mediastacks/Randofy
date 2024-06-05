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


def fetch_all_categories(sp):
    #Fetches all categories from Spotify and saves to a file.
    all_categories = []
    offset = 0
    limit = 50  # Maximum allowed by Spotify API
    
    while True:
        categories = sp.categories(limit=limit, offset=offset)['categories']['items']
        if not categories:
            break
        all_categories.extend(categories)
        offset += limit
        
    # Get the script's directory
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Construct the file path relative to the script's directory
    file_path = os.path.join(script_dir, 'categories.txt')
    
    # Write all categories to the file
    with open(file_path, 'w') as file:
        for category in all_categories:
            file.write(f"{category['id']} - {category['name']}\n")
    
    print("Fetched categories from Spotify and saved to file.")
    
    return all_categories

def get_all_categories_from_file():
    #Reads categories from the file.
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'categories.txt')
    
    categories = []
    with open(file_path, 'r') as file:
        for line in file:
            category_id, category_name = line.strip().split(' - ', 1)
            categories.append({'id': category_id, 'name': category_name})
    
    print("Read categories from file.")
    return categories

def get_random_track(sp):
    try:
        # Get the script's directory
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, 'categories.txt')
        
        # Check if the categories.txt file exists
        if os.path.exists(file_path):
            # Read categories from the file
            categories = get_all_categories_from_file()
        else:
            # Fetch categories from Spotify and save to the file
            categories = fetch_all_categories(sp)
        
        if not categories:
            print("No categories found.")
            return None
        
        # Now you have all categories, select one randomly
        category = random.choice(categories)['id']
    
        # Fetch a random playlist from the chosen category
        playlists = sp.category_playlists(category_id=category, limit=50)['playlists']['items']
        playlist = random.choice(playlists)['id']
        
        # Fetch the tracks from the chosen playlist
        tracks = sp.playlist_tracks(playlist, limit=100)['items']
        
        # Initialize empty lists for tracks in each popularity range
        low_popularity_tracks = []
        high_popularity_tracks = []
        
        # Populate lists based on track popularity
        for track in tracks:
            if 1 <= track['track']['popularity'] <= 35:
                low_popularity_tracks.append(track)
            elif track['track']['popularity'] > 35:
                high_popularity_tracks.append(track)
        
        # Check if there are enough tracks in each range
        if len(low_popularity_tracks) > 0 and len(high_popularity_tracks) > 0:
            # Weighted choice between popularity ranges
            if random.random() < 0.7:  # 70% chance to choose from lower popularity tracks
                selected_tracks = low_popularity_tracks
            else:  # 30% chance to choose from high popularity tracks
                selected_tracks = high_popularity_tracks
        elif len(low_popularity_tracks) > 0:
            selected_tracks = low_popularity_tracks
        elif len(high_popularity_tracks) > 0:
            selected_tracks = high_popularity_tracks
        else:
            print("Not enough tracks found in either popularity range.")
            return None  # Or handle this case as appropriate
        
        # Select a random track from the chosen range
        track = random.choice(selected_tracks)['track']
        
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
