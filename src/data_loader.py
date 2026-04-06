import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (local)
load_dotenv()

# Nomes CORRETOS das 40 colunas (o header original tem 39 porque juntou "Discount" e "DLC count")
CORRECT_COLUMNS = [
    'AppID', 'Name', 'Release date', 'Estimated owners', 'Peak CCU',
    'Required age', 'Price', 'Discount', 'DLC count', 
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
    Carrega o dataset da Steam com fallback inteligente:
    1. Tenta carregar arquivo LOCAL (.csv ou .parquet)
    2. Se não encontrar localmente, tenta baixar do Google Drive via URL segura.
    """
    
    # 1. Tentar ler Parquet local (muito mais rápido, se existir)
    parquet_path = file_path.replace(".csv", ".parquet")
    if os.path.exists(parquet_path):
        print(f"✅ Carregando arquivo PARQUET local: {parquet_path}")
        return pd.read_parquet(parquet_path)

    # 2. Tentar ler CSV local
    if os.path.exists(file_path):
        print(f"📦 Carregando arquivo CSV local: {file_path}")
        return pd.read_csv(file_path, header=0, names=CORRECT_COLUMNS)

    # 3. Fallback para Google Drive (Remoto)
    # Busca em st.secrets (Nuvem) ou os.getenv (.env local)
    drive_id = st.secrets.get("GOOGLE_DRIVE_ID") if "GOOGLE_DRIVE_ID" in st.secrets else os.getenv("GOOGLE_DRIVE_ID")
    
    if drive_id and drive_id != "COLE_O_ID_AQUI":
        drive_url = f'https://drive.google.com/uc?export=download&id={drive_id}'
        st.info("🌐 Arquivo local não encontrado. Carregando dados do Google Drive...")
        return pd.read_csv(drive_url, header=0, names=CORRECT_COLUMNS)
    
    # Se nada funcionar
    return None
