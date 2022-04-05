import streamlit as st
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------
# To run locally run: 'streamlit run pokemon_color.py'
# ----------------------------------------------------------------------------------------------------------------------

@st.cache
def load_contexte(path):
    with open(path,'r', encoding='utf-8') as file:
        data = file.read()
    return data


st.sidebar.image("https://stock.wikimini.org/w/images/2/2c/Pok%C3%A9mon.gif")

# Add data from API: https://pokeapi.co/api/v2/pokemon/abra

    