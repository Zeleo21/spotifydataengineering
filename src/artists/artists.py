from spotifydataengineering.src.spotify import SpotifyConfig
from spotifydataengineering.src.db import DBConfig

sp = SpotifyConfig()
db = DBConfig()

def get_top_artists(offset=0, limit=10, time_range='medium_term'):
    results = sp.current_user_top_artists(limit=limit, offset=offset, time_range=time_range)
    artists = []
    for idx, item in enumerate(results['items']):
        artist = {
            'name': item['name'],
            'genres': item['genres'],
            'popularity': item['popularity'],
            'followers': item['followers']['total'],
            'link': item['external_urls']['spotify']
        }
        artists.append(artist)
        print(f"{idx + 1}: {artist['name']} - {artist['popularity']}")
        print(f"Genres: {', '.join(artist['genres'])}")
        print(f"Followers: {artist['followers']}")
        print(f"Link: {artist['link']}")
    return artists