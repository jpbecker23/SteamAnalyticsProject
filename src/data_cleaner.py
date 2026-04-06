import pandas as pd
import numpy as np

def clean_steam_data(df):
    """
    Limpa e transforma o dataframe da Steam de forma resiliente.
    Funciona com o dataset completo ou com a versão Slim.
    """
    if df is None:
        return None
    
    df_clean = df.copy()
    
    if 'Name' in df_clean.columns:
        df_clean['Name'] = df_clean['Name'].fillna('Unknown Game').astype(str).str.strip()
    
    if 'Price' in df_clean.columns:
        df_clean['Price'] = pd.to_numeric(df_clean['Price'], errors='coerce').fillna(0.0)
        
        def categorize_price(price):
            if price == 0: return 'Gratuito'
            elif price < 10: return 'Econômico (<$10)'
            elif price < 30: return 'Padrão ($10-$30)'
            else: return 'Premium (>$30)'
        df_clean['Price_Category'] = df_clean['Price'].apply(categorize_price)

    if 'Positive' in df_clean.columns and 'Negative' in df_clean.columns:
        df_clean['Positive'] = pd.to_numeric(df_clean['Positive'], errors='coerce').fillna(0).astype(int)
        df_clean['Negative'] = pd.to_numeric(df_clean['Negative'], errors='coerce').fillna(0).astype(int)
        df_clean['Total_Reviews'] = df_clean['Positive'] + df_clean['Negative']
        
        df_clean['Review_Score'] = 0.0
        mask = df_clean['Total_Reviews'] > 0
        df_clean.loc[mask, 'Review_Score'] = (df_clean.loc[mask, 'Positive'] / df_clean.loc[mask, 'Total_Reviews']) * 100
        df_clean['Review_Score'] = df_clean['Review_Score'].round(1)

    if 'Release date' in df_clean.columns:
        df_clean['Release_Date_DT'] = pd.to_datetime(df_clean['Release date'], errors='coerce')
        df_clean['Release_Year'] = df_clean['Release_Date_DT'].dt.year.fillna(0).astype(int)
    if 'Main_Genre' not in df_clean.columns and 'Genres' in df_clean.columns:
        df_clean['Main_Genre'] = df_clean['Genres'].fillna('Outros').apply(lambda x: str(x).split(',')[0].strip())
    
    if 'Main_Genre' in df_clean.columns:
        df_clean['Main_Genre'] = df_clean['Main_Genre'].fillna('Outros').astype(str).str.strip()
    else:
        df_clean['Main_Genre'] = 'Outros'

    return df_clean
