from spotifydataengineering.src.artists.artists_helper import format_genres
from spotifydataengineering.src.spotify import SpotifyConfig
from spotifydataengineering.src.db import DBConfig
import uuid

sp = SpotifyConfig()
db = DBConfig()

def get_top_artists(offset=0, limit=10, time_range='medium_term'):
    results = sp.current_user_top_artists(limit=limit, offset=offset, time_range=time_range)
    artists = []
    for idx, item in enumerate(results['items']):
        print(item)
        artists.append(item)
    return artists

def insert_top_artists(artists):
    for artist in artists:
        db.cursor.execute("SELECT artist_id FROM artist WHERE artist_id = %s", (artist['id'],))
        existing_artist = db.cursor.fetchone()
        if existing_artist:
            continue
        new_id = str(uuid.uuid4())
        genres = format_genres(artist['genres'])
        db.cursor.execute(
            "INSERT INTO artist (id, name, genres, popularity, type ,uri, artist_id, href, followers, spotify_url) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (new_id, artist['name'], genres , artist['popularity'], artist['type'], artist['uri'], artist['id'], artist['href'], artist['followers']['total'], artist['external_urls']['spotify'])
        )
    db.conn.commit()
    print("Top artists inserted into the database.")


# TODO Delete function -> delete_top_artists