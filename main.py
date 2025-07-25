from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd
from datetime import date
from fastapi.responses import JSONResponse


app = FastAPI()

class MovieInput(BaseModel):
    context: Annotated[str, Field(..., description="Name of the Movie")]



@app.post('/recommend')
def recommend(data: MovieInput):

    # print(data)
    recommendation = "Avatar"
    return JSONResponse(status_code=200, content={'movies': recommendation})