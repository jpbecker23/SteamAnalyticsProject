import pandas as pd

def clean_steam_data(df):
    """
    Limpa e transforma o dataframe bruto da Steam para análise.
    """
    if df is None:
        return None
    
    # Fazendo cópia para evitar warnings
    df_clean = df.copy()
    
    # 1. Selecionar colunas essenciais para o MVP
    cols_to_keep = ['Name', 'Release date', 'Price', 'Positive', 'Negative', 'Genres', 'Categories']
    df_clean = df_clean[cols_to_keep]
    
    # 2. Tratar Nomes Vazios e Limpeza
    df_clean['Name'] = df_clean['Name'].fillna('Unknown Game').astype(str).str.strip()
    
    # 3. Tratar Preços (preencher nulos com 0 e converter para float)
    df_clean['Price'] = pd.to_numeric(df_clean['Price'], errors='coerce').fillna(0.0)
    
    # 4. Tratar Reviews
    df_clean['Positive'] = pd.to_numeric(df_clean['Positive'], errors='coerce').fillna(0).astype(int)
    df_clean['Negative'] = pd.to_numeric(df_clean['Negative'], errors='coerce').fillna(0).astype(int)
    df_clean['Total_Reviews'] = df_clean['Positive'] + df_clean['Negative']
    
    # 5. Calcular Score de Avaliação (Proxy: % de reviews positivas)
    df_clean['Review_Score'] = 0.0
    mask = df_clean['Total_Reviews'] > 0
    df_clean.loc[mask, 'Review_Score'] = (df_clean.loc[mask, 'Positive'] / df_clean.loc[mask, 'Total_Reviews']) * 100
    df_clean['Review_Score'] = df_clean['Review_Score'].round(1) # Arredondar para 1 casa decimal
    
    # 6. Extrair Ano de Lançamento
    df_clean['Release_Date_DT'] = pd.to_datetime(df_clean['Release date'], errors='coerce')
    df_clean['Release_Year'] = df_clean['Release_Date_DT'].dt.year.fillna(0).astype(int)
    
    # 7. Categorizar Preços
    def categorize_price(price):
        if price == 0: return 'Gratuito'
        elif price < 10: return 'Econômico (<$10)'
        elif price < 30: return 'Padrão ($10-$30)'
        else: return 'Premium (>$30)'
        
    df_clean['Price_Category'] = df_clean['Price'].apply(categorize_price)
    
    # 8. Limpeza de Gêneros (pegar o primeiro gênero principal)
    df_clean['Main_Genre'] = df_clean['Genres'].fillna('Outros').apply(lambda x: str(x).split(',')[0].strip())
    
    # Debug: Mostrar colunas finais
    print(f"Dados limpos! Colunas disponíveis: {df_clean.columns.tolist()}")
    
    return df_clean
