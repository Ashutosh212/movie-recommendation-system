import pandas as pd

def build_movie_text(row):
    parts = [
        f"Genres: {" ".join(row['genres'])}",
        f"Keywords: {', '.join(row['keywords'])}",
        f"Overview: {row['overview']}",
        f"Production Companies: {', '.join(row['production_companies'])}",
        f"Cast: {', '.join(row['cast'])}",
        f"Director: {row['crew']}",
    ]
    return " ".join(parts)