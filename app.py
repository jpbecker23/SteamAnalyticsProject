import streamlit as st
import plotly.express as px
from src.data_loader import load_data
from src.data_cleaner import clean_steam_data
import os

# Configuração da página
st.set_page_config(page_title="Steam Analytics Dashboard", page_icon="🎮", layout="wide")

# Caminho do arquivo
DATA_PATH = "data/raw/games.csv"

# Carregamento e Limpeza
if os.path.exists(DATA_PATH):
    # Carregando dados
    df_raw = load_data(DATA_PATH)
    df = clean_steam_data(df_raw)
    
    # Título Principal
    st.title("🎮 Steam Analytics Dashboard")
    st.markdown("---")


    # Sidebar para filtros
    st.sidebar.header("Filtros do Dashboard")
    
    # Filtro de Ano de Lançamento
    valid_years = df[df['Release_Year'] > 0]['Release_Year']
    min_year = int(valid_years.min()) if not valid_years.empty else 1997
    max_year = int(df['Release_Year'].max()) if not df['Release_Year'].empty else 2025
    year_range = st.sidebar.slider("Ano de Lançamento", min_year, max_year, (2010, max_year))
    
    # Filtro de Faixa de Preço
    max_price = float(df['Price'].max())
    price_range = st.sidebar.slider("Faixa de Preço (US$)", 0.0, max_price, (0.0, 100.0 if max_price > 100 else max_price))
    
    # Aplicando Filtros
    df_filtered = df[
        (df['Price'] >= price_range[0]) & 
        (df['Price'] <= price_range[1]) &
        (df['Release_Year'] >= year_range[0]) &
        (df['Release_Year'] <= year_range[1])
    ]

    # KPI Cards Dinâmicos
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Jogos", f"{len(df_filtered):,}")
    with col2:
        st.metric("Preço Médio", f"US$ {df_filtered['Price'].mean():.2f}")
    with col3:
        st.metric("Satisfação Média", f"{df_filtered['Review_Score'].mean():.1f}%")

    st.markdown("---")

    # Layout de Gráficos
    col_g1, col_g2 = st.columns(2)

    with col_g1:
        st.subheader("🔥 Top 20 Jogos Mais Populares")
        # Usando Total_Reviews como proxy de popularidade
        top_20 = df_filtered.nlargest(20, 'Total_Reviews').sort_values('Total_Reviews', ascending=True)
        
        fig_pop = px.bar(
            top_20, 
            x='Total_Reviews', 
            y='Name', 
            orientation='h',
            color='Review_Score',
            color_continuous_scale='Viridis',
            text='Total_Reviews', 
            labels={'Total_Reviews': 'Total de Avaliações', 'Name': 'Nome do Jogo', 'Review_Score': 'Pontuação (%)'},
            template='plotly_dark',
            hover_data={
                'Name': False, 
                'Total_Reviews': ':,', 
                'Review_Score': ':.1f'
            }
        )
        
        # Melhorias visuais
        fig_pop.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig_pop.update_layout(
            yaxis={'title': ''}, 
            margin=dict(l=200), 
            height=600,
            coloraxis_colorbar=dict(title="Score %")
        )
        st.plotly_chart(fig_pop, width='stretch')

    with col_g2:
        st.subheader("💰 Relação Preço vs Avaliação")
        # Amostragem para performance
        df_sample = df_filtered.sample(min(5000, len(df_filtered))) if len(df_filtered) > 5000 else df_filtered
        
        fig_price = px.scatter(
            df_sample,
            x='Price',
            y='Review_Score',
            color='Price_Category',
            size='Total_Reviews',
            hover_name='Name',
            hover_data={'Price': ':.2f', 'Review_Score': ':.1f', 'Total_Reviews': ':,'},
            labels={'Price': 'Preço (US$)', 'Review_Score': 'Pontuação (%)', 'Price_Category': 'Categoria'},
            template='plotly_dark',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_price.update_layout(height=600)
        st.plotly_chart(fig_price, width='stretch')

else:
    st.error("❌ Arquivo data/raw/games.csv não encontrado!")
    st.info("Por favor, coloque o arquivo baixado do Kaggle na pasta correta.")
