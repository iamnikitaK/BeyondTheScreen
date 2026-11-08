import streamlit as st
import pickle
import pandas as pd
import requests
import os
from sklearn.metrics.pairwise import cosine_similarity

from scipy.sparse import load_npz

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movies = pickle.load(
    open(os.path.join(BASE_DIR, 'movies.pkl'), 'rb')
)

vectors = load_npz(
    os.path.join(BASE_DIR, 'vectors.npz')
)


try:
    TMDB_API_KEY = os.getenv("TMDB_API_KEY") or st.secrets["TMDB_API_KEY"]
except Exception:
    TMDB_API_KEY = None


if TMDB_API_KEY:
    print("TMDB API Key: FOUND")
    print("API Key length:", len(TMDB_API_KEY))
else:
    print("TMDB API Key: NOT FOUND")


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    if not TMDB_API_KEY:
        return None

    try:
        response = requests.get(
            url,
            params={
                "api_key": TMDB_API_KEY,
                "language": "en-US"
            },
            timeout=15
        )

        response.raise_for_status()
        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path

        return None

    except requests.exceptions.RequestException as e:
        print(f"TMDB request failed for movie {movie_id}: {e}")
        return None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = cosine_similarity(
        vectors[movie_index],
        vectors
    ).flatten()

    recommendations = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in recommendations:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


# Get movie titles
movie_titles = movies['title'].values


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movie_titles
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        if posters[0] is not None:
            st.image(posters[0])
        else:
            st.write("Poster unavailable")

    with col2:
        st.text(names[1])
        if posters[1] is not None:
            st.image(posters[1])
        else:
            st.write("Poster unavailable")

    with col3:
        st.text(names[2])
        if posters[2] is not None:
            st.image(posters[2])
        else:
            st.write("Poster unavailable")

    with col4:
        st.text(names[3])
        if posters[3] is not None:
            st.image(posters[3])
        else:
            st.write("Poster unavailable")

    with col5:
        st.text(names[4])
        if posters[4] is not None:
            st.image(posters[4])
        else:
            st.write("Poster unavailable")
