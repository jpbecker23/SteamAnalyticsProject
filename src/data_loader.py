import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

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
    
    parquet_path = file_path.replace(".csv", ".parquet")
    if os.path.exists(parquet_path):
        print(f"✅ Carregando arquivo PARQUET local: {parquet_path}")
        return pd.read_parquet(parquet_path)

    if os.path.exists(file_path):
        print(f"📦 Carregando arquivo CSV local: {file_path}")
        return pd.read_csv(file_path, header=0, names=CORRECT_COLUMNS)

    drive_id = st.secrets.get("GOOGLE_DRIVE_ID") if "GOOGLE_DRIVE_ID" in st.secrets else os.getenv("GOOGLE_DRIVE_ID")
    
    if drive_id and drive_id != "COLE_O_ID_AQUI":
        drive_url = f'https://drive.google.com/uc?export=download&id={drive_id}'
        st.info("🌐 Arquivo local não encontrado. Carregando dados do Google Drive... (Isso pode levar alguns segundos)")
        
        try:
            return pd.read_parquet(drive_url)
        except Exception:
            try:
                return pd.read_csv(drive_url, header=0, names=CORRECT_COLUMNS)
            except Exception as e:
                st.error(f"❌ Erro ao processar o arquivo do Google Drive: {e}")
                st.info("💡 Verifique se o link do arquivo no Drive está como 'Qualquer pessoa com o link pode visualizar'.")
                return None
    
    return None
