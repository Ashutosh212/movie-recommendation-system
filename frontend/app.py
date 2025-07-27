import streamlit as st
import requests
import pandas as pd
import sys

sys.path.append(".")

from backend.preprocess import build_movie_text

API_URL = "http://127.0.0.1:8000/recommend"


df_final = pd.read_csv("dataset/df_final.csv")

df_final = df_final[:100]

st.title("Movie Recommender System")

st.markdown("Fill out the movie name from the list or share the detail of the movie you want to watch today")


movie_list = tuple(df_final['title'])

option = st.selectbox(
    "Which movie you like to watch?",
    movie_list,
    index=None,
    placeholder="Example: Avatar, The Dark Knight Rises",
)

# st.write("You selected:", option)

st.write("OR")

# "AND" # This is the magic command 

movie_type = st.text_area(
    label="Describe the Type of Movie You Want to Watch",
    placeholder="Example: Today, I'd like to watch a sci-fi movie with superheroes or space battles.",
    height=200
)
  

recommended_movies = """
## Hey your top five movies will be:
1. **Avatar**
2. **Star War**
"""


if st.button("Recommend Movies", type="primary",icon=":material/movie:"):
    
    if option is not None:
        row = df_final[(df_final['title'] == option)]
        # st.write(row)
        context = build_movie_text(row)
      
    else:
        context = movie_type

    data = {
        'context': context
    }

    try:
        response = requests.post(API_URL, json=data)
        result = response.json()

        if response.status_code == 200:
            st.success(f"Recommended Movies")
            for i, movie_dict in enumerate(result["recommendations"]):
                
                st.write(f"{i+1}: **{movie_dict["Title"]}**")
                with st.expander("Overview"):
                    st.write(movie_dict["Overview"])

        else:
            st.error("Prediction failed. Check API or input format.")
            st.json(result)

            st.error("Prediction failed. Check API or input format.")
            st.json(result)

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI server. Make sure it's running.")
