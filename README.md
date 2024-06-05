#  Randofy: Spice Up Your Music Life 🎲 🎵

 ![randofy](https://github.com/mediastacks/Randofy/assets/69261677/fdd82592-bed2-4801-af48-bdf61d47c14c)


**Randofy** is a fun little Python script designed to broaden your musical horizons by playing a random song from the Spotify catalog. It's your personal DJ who always surprises you with something new! 🎧✨

### How It Works

1. **Login to Spotify**: Uses your dev credentials to log into Spotify [(you can get them here)](https://developer.spotify.com/)
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

3. **Run the Script**:
    ```bash
    python randofy.py
    ```

### Why Use Randofy?

- **Broaden Your Horizons**: Discover new music you might never have found otherwise! 🌍🎵
- **Fun and Surprising**: Never know what you'll get next, that can be fun! 🎉

### Optional: Desktop Shortcut

You may use the included icon png or ico if you wish to make a destop shortcut for the script.

Have fun! ❤️
