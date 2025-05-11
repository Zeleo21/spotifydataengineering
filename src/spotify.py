from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyConfig:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            load_dotenv()
            scope = ('user-library-read user-top-read playlist-read-private playlist-read-collaborative '
                     'user-read-private user-read-email user-follow-read user-read-playback-state '
                     'user-modify-playback-state user-read-currently-playing user-read-recently-played')
            cls._instance = super(SpotifyConfig, cls).__new__(cls)
            cls._instance.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        return cls._instance.sp