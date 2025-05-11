

def format_genres(genres):
    """
    Format the genres from a list to a string.
    """
    if not genres:
        return None
    return ', '.join(genres)