import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

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


def get_embedding(text: str):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small",
        dimensions=256
    )
    return response.data[0].embedding