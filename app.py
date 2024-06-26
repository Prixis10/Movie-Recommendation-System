import streamlit as st #type: ignore
import pickle
import pandas as pd #type: ignore
import requests #type: ignore

# def fetch_poster(movie_id):
#     response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=2fdc52d8885026845e7e1a5dcf3cae59".format(movie_id))
#     data = response.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     8265bd1679663a7ea12ac168da84d2e8&language=en-US
#     return full_path

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2fdc52d8885026845e7e1a5dcf3cae59".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


movies_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))

#st.title('Movie Recommender System')

#st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide", initial_sidebar_state="expanded")
st.set_page_config(page_title="Movie Recommender System", page_icon="🎬")
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Type or select a movie from dropdown',
    movies['title'].values)

if st.button('Recommend'):
    st.write('The recommended movies are: ')
    names,posters = recommend(selected_movie_name)
    # for i in names:
    #     st.write(i)  
    columns = st.columns(5)
    for poster, name, column in zip(posters,names,columns):
        with column:
            st.image(poster)
            st.write(name)