import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from spotifydataengineering.src.db import DBConfig

load_dotenv()

scope = 'user-library-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def get_current_user_saved_tracks():
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(f"{idx + 1}: {track['name']} - {track['artists'][0]['name']}")
        print(f"Album: {track['album']['name']}")
        print(f"Release Date: {track['album']['release_date']}")
        print(f"Link: {track['external_urls']['spotify']}")


print(sp.current_user())
# get_current_user_saved_tracks()


db = DBConfig()
db.execute("SELECT * FROM test;")
print(db.fetchall())