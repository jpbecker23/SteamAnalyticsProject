import streamlit as st
from src.data_loader import load_data
from src.data_cleaner import clean_steam_data
from src.charts import plot_top_popular, plot_price_vs_rating
import os

st.set_page_config(page_title="Steam Analytics Dashboard", page_icon="🎮", layout="wide")

DATA_PATH = "data/raw/games.csv"

df_raw = load_data(DATA_PATH)

if df_raw is not None:
    df = clean_steam_data(df_raw)
    
    st.title("🎮 Steam Analytics Dashboard")
    st.markdown("---")

    st.sidebar.header("Filtros do Dashboard")
    
    valid_years = df[df['Release_Year'] > 0]['Release_Year']
    min_year = int(valid_years.min()) if not valid_years.empty else 1997
    max_year = int(df['Release_Year'].max()) if not df['Release_Year'].empty else 2025
    year_range = st.sidebar.slider("Ano de Lançamento", min_year, max_year, (2010, max_year))
    
    max_price = float(df['Price'].max())
    price_range = st.sidebar.slider("Faixa de Preço (US$)", 0.0, max_price, (0.0, 100.0 if max_price > 100 else max_price))
    
    all_genres = sorted(df['Main_Genre'].unique().tolist())
    selected_genres = st.sidebar.multiselect("Filtrar por Gêneros", all_genres, default=[])

    df_filtered = df[
        (df['Price'] >= price_range[0]) & 
        (df['Price'] <= price_range[1]) &
        (df['Release_Year'] >= year_range[0]) &
        (df['Release_Year'] <= year_range[1])
    ]
    
    if selected_genres:
        df_filtered = df_filtered[df_filtered['Main_Genre'].isin(selected_genres)]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Jogos", f"{len(df_filtered):,}")
    with col2:
        st.metric("Preço Médio", f"US$ {df_filtered['Price'].mean():.2f}")
    with col3:
        st.metric("Satisfação Média", f"{df_filtered['Review_Score'].mean():.1f}%")

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["🔥 Panorama Geral", "💰 Análise de Preços", "🔍 Explorador de Dados"])

    with tab1:
        st.plotly_chart(plot_top_popular(df_filtered), width='stretch')

    with tab2:
        st.plotly_chart(plot_price_vs_rating(df_filtered), width='stretch')
        st.info("💡 Dica: No gráfico acima, o tamanho dos círculos representa a popularidade total do jogo.")

    with tab3:
        st.subheader("Visualização dos Dados Filtrados")
        st.dataframe(
            df_filtered[['Name', 'Release date', 'Price', 'Total_Reviews', 'Review_Score', 'Main_Genre']],
            use_container_width=True,
            hide_index=True
        )

else:
    st.error("❌ Dados não encontrados!")
    st.info("O arquivo local 'data/raw/games.csv' não foi detectado e o Google Drive ID não foi configurado corretamente nos Secrets do Streamlit Cloud.")
