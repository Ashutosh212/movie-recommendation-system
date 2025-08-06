import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd
from datetime import date
import traceback
from fastapi.responses import JSONResponse
from .preprocess import get_embedding

app = FastAPI()

df_final = pd.read_csv("dataset/df_final.csv")

df_final = df_final[:100]

class MovieInput(BaseModel):
    context: Annotated[str, Field(..., description="Name of the Movie")]
@app.get('/')
def home():
    return "Welcome to Recommendation Project"

@app.post('/recommend')
def recommend(data: MovieInput):

    # print(data)
    context = data.context

    embedding_matrix = np.load("results/movie_embeddings.npy")

    norms = np.linalg.norm(embedding_matrix, axis=1, keepdims=True) # What is this `linalg.norm`
    normalized_matrix = embedding_matrix / norms

    query = get_embedding(context)
    query = query / np.linalg.norm(query)

    # Compute cosine similarities
    scores = np.dot(normalized_matrix, query)

    # Get top-k
    top_k_idx = np.argsort(-scores)[:6]  # What is this `argsort`

    try:
        movie_dict = []
        first = False
        for i in top_k_idx:
            if not first:
                first = True
                continue
            curr_dict = {
                "Title": df_final.iloc[i]['title'],
                "Overview": [df_final.iloc[i]['overview']]
            }
            movie_dict.append(curr_dict)

        return JSONResponse(status_code=200, content={"recommendations": movie_dict})

    except Exception as e:
        print("❌ Error in /recommend:", e)
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})

