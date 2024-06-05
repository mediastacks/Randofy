#  Randofy: Spice Up Your Music Life 🎲 🎵

![randofyyyyyy(1)](https://github.com/mediastacks/Randofy/assets/69261677/c34980e3-39ec-4b68-b580-4e2b9a488ac0)




**Randofy** is a fun little Python script designed to broaden your musical horizons by playing a random song from the Spotify catalog. It's your personal DJ who always surprises you with something new! 🎧✨

### How It Works

1. **Logins to Spotify**: Uses your dev credentials to log in [(you can get them here)](https://developer.spotify.com/)
2. **Picks a Random Song**: Selects a random music category, then a random playlist within that category, and finally a random song from that playlist.
3. **Plays It**: Finds your active Spotify device and starts playing the selected song. 🎶

### Setup

1. **Install Required Libraries**:
    ```bash
    pip install spotipy python-dotenv
    ```

2. **Set Up `.env` File**: Edit the `.env` file and insert your Spotify credentials:
    ```ini
    SPOTIPY_CLIENT_ID=your_spotify_client_id
    SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
    SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
    SPOTIPY_USERNAME=your_spotify_username
    ```
### Usage

1. **Run the Script**:
    ```bash
    python randofy.py
    ```
2. **Have Fun!** ✨

### Customization

**Categories**: Upon initial run you will get categories.txt in the script's folder - you can remove categories you don't want.


### Why Use Randofy?

- **Broaden Your Horizons**: Discover new music you might never have found otherwise! 🌍🎵
- **Fun and Surprising**: Never know what you'll get next, it can be fun! 🎉

### Optional: Desktop Icons

You may use the included png or ico images if you wish to make a destop shortcut for the script.

Note: given the way it works, only songs added to playlists will be picked, so it's less likely to encounter non-popular tracks.
