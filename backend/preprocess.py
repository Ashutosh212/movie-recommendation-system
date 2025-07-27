import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os
# load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not set. Please provide it via environment variable.")

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
