from spotifydataengineering.src.artists.artists import get_top_artists, insert_top_artists
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


# This is a simple main for now
# -> plans to have a little CLI for the user to choose what they want to do with the data
def main():
    artists = get_top_artists()
    insert_top_artists(artists)

if __name__ == "__main__":
    main()