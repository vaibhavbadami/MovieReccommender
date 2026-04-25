import pickle
import streamlit as st
import requests
import pandas as pd
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_home = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_t24tpvcu.json")
lottie_details = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_gja1z3cr.json")

def fetch_poster(movie_title):
    api_key = '80e6682'
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    poster_url = data.get('Poster')
    return poster_url if poster_url and poster_url != "N/A" else "https://via.placeholder.com/300x450?text=No+Image+Available"

def fetch_movie_details(movie_title):
    api_key = '80e6682'
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data.get('Response') == 'True':
        return {
            'Title': data.get('Title', 'N/A'),
            'Year': data.get('Year', 'N/A'),
            'Genre': data.get('Genre', 'N/A'),
            'Director': data.get('Director', 'N/A'),
            'Actors': data.get('Actors', 'N/A'),
            'Plot': data.get('Plot', 'N/A'),
            'imdbRating': data.get('imdbRating', 'N/A'),
            'Runtime': data.get('Runtime', 'N/A'),
            'Poster': data.get('Poster')
        }
    return None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movie_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movie_names.append(movie_title)
        recommended_movie_posters.append(fetch_poster(movie_title))

    return recommended_movie_names, recommended_movie_posters

st.set_page_config(page_title="Movie Recommender", page_icon="🍿", layout="wide")

st.markdown("""
    <style>
    .poster-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .poster-card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0,0,0,0.4);
    }
    </style>
""", unsafe_allow_html=True)

movies_data = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_data)
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_list = movies['title'].values

if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'clicked_movie' not in st.session_state:
    st.session_state.clicked_movie = None

if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None

def go_to_home():
    st.session_state.page = 'home'
    st.session_state.clicked_movie = None

def go_to_details(movie_title):
    st.session_state.clicked_movie = movie_title
    st.session_state.page = 'details'

if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align:center;color:#FF4B4B;'>🎬 Movie Recommender System 🍿</h1>", unsafe_allow_html=True)
    if lottie_home:
        st_lottie(lottie_home, height=200)

    selected_movie = st.selectbox("🎥 Select a movie to get recommendations:", movie_list)

    if st.button('🔍 Show Recommendations'):
        names, posters = recommend(selected_movie)
        st.session_state.recommendations = (names, posters)

    if st.session_state.recommendations:
        names, posters = st.session_state.recommendations
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                if col.button(' ', key=f"poster_{idx}"):
                    go_to_details(names[idx])
                col.markdown(f"""
                    <div class="poster-card">
                        <img src="{posters[idx]}" style="width:100%; border-radius:10px;">
                    </div>
                    <div style='text-align:center;font-weight:bold;color:white;background-color:#4B4B4B;border-radius:10px;padding:8px;margin-top:5px;'>
                        {names[idx]}
                    </div>
                """, unsafe_allow_html=True)

elif st.session_state.page == 'details':
    details = fetch_movie_details(st.session_state.clicked_movie)
    st.markdown(f"<h2 style='text-align:center;'>{details['Title']} ({details['Year']})</h2>", unsafe_allow_html=True)
    if lottie_details:
        st_lottie(lottie_details, height=150)

    st.image(details['Poster'], width=250)
    st.markdown(f"**Genre:** {details['Genre']}")
    st.markdown(f"**Director:** {details['Director']}")
    st.markdown(f"**Actors:** {details['Actors']}")
    st.markdown(f"**IMDb Rating:** ⭐ {details['imdbRating']}")
    st.markdown(f"**Runtime:** {details['Runtime']}")
    st.markdown(f"**Plot:** {details['Plot']}")

    if st.button('🔙 Back to Home'):
        go_to_home()

st.markdown("<hr style='border: 1px solid #FF4B4B;'>", unsafe_allow_html=True)
