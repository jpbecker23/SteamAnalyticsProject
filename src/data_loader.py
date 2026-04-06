import pandas as pd
import streamlit as st
import os

# Nomes CORRETOS das 40 colunas (o header original tem 39 porque juntou "Discount" e "DLC count")
CORRECT_COLUMNS = [
    'AppID', 'Name', 'Release date', 'Estimated owners', 'Peak CCU',
    'Required age', 'Price', 'Discount', 'DLC count',  # <-- Separados corretamente
    'About the game', 'Supported languages', 'Full audio languages',
    'Reviews', 'Header image', 'Website', 'Support url', 'Support email',
    'Windows', 'Mac', 'Linux', 'Metacritic score', 'Metacritic url',
    'User score', 'Positive', 'Negative', 'Score rank', 'Achievements',
    'Recommendations', 'Notes', 'Average playtime forever',
    'Average playtime two weeks', 'Median playtime forever',
    'Median playtime two weeks', 'Developers', 'Publishers',
    'Categories', 'Genres', 'Tags', 'Screenshots', 'Movies'
]

@st.cache_data
def load_data(file_path):
    """
    Carrega o dataset da Steam de um arquivo CSV.
    Corrige o desalinhamento de colunas do CSV original.
    Usa o cache do Streamlit para performance.
    """
    if not os.path.exists(file_path):
        return None
    
    # Pular o header original (que tem 39 colunas) e usar os nomes corretos (40 colunas)
    df = pd.read_csv(file_path, header=0, names=CORRECT_COLUMNS)
    
    print(f"Dataset carregado: {len(df)} jogos, {len(df.columns)} colunas")
    return df
