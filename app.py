import streamlit as st
import pickle 
import pandas as pd

def recommend(game):
    game_index = games[games['name'] == game].index[0]
    distances = similiarity[game_index]
    game_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_games = []
    recommended_posters = []
    for i in game_list:
        game_id = games.iloc[i[0]]['appid']
        game_data = games_metadata[games_metadata['appid'] == game_id]
        recommended_games.append(game_data['name'].values[0])
        recommended_posters.append(game_data['header_image'].values[0])
    return recommended_games,recommended_posters

games = pickle.load(open('stream_games.pkl','rb'))
similiarity = pickle.load(open('similiarity.pkl','rb'))
games_metadata = pickle.load(open('games_metadata.pkl', 'rb'))

st.title('Game Recommendation System')
selected_game_name = st.selectbox('Wanna See games similar to your taste?? : ',games['name'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_game_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            st.image(posters[i], width=300,)
            st.caption(names[i])