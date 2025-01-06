import streamlit as st
import pandas as pd
import requests
import pickle

with open('movies.pkl','rb') as file:
    movies,cosine_sim=pickle.load(file)
    
def recommendation(title,cosine_sim=cosine_sim):
  index=movies[movies['title']==title].index[0]
  sim_scores=list(enumerate(cosine_sim[index]))
  sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
  sim_scores=sim_scores[1:11]  #get top 10 similar movies
  movie_index=[i[0] for i in sim_scores]
  return movies['title'].iloc[movie_index]

def fetchPoster(movie_id):
   api_key='f46bd19le14f0b6d024fa0f6e09le706'
   url= f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api-key}'
   response=requests.get(url)
   data=response.json()
   poster_path=data['poster_path']
   full_path=f"https://image.tmdb.org/t/p/w500{poster_path}"
   return full_path

   st.title("Movie Recommendation System")

   selected_movie=st.selectbox("Select a movie:",movies['title'].values)

   if st.button('Recommend'):
    recommended_movies=recommendation(selected_movie)
    st.write("Recommended Movies")

    for i in range(0,10,5):
      cols=at.columns(5)
      for col,j in zip(cols,range(i,i+5)):
        if j<len(recommended_movie):
          movie_title=recommended_movie.iloc[j]['title']
          movie_id=recommended_movie.iloc[j]['movie_id']
          poster_path=fetchPoster(movie_id)
          with col:
            st.image(poster_path,width=130)
            st.write(movie_title)