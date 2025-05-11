from spotifydataengineering.src.artists.artists import get_top_artists
from spotifydataengineering.src.db import DBConfig
from spotifydataengineering.src.spotify import SpotifyConfig

sp = SpotifyConfig()

def get_current_user_saved_tracks():
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(f"{idx + 1}: {track['name']} - {track['artists'][0]['name']}")
        print(f"Album: {track['album']['name']}")
        print(f"Release Date: {track['album']['release_date']}")
        print(f"Link: {track['external_urls']['spotify']}")


print(sp.current_user())
#get_current_user_saved_tracks()
get_top_artists()

db = DBConfig()
db.execute("SELECT * FROM test;")
print(db.fetchall())