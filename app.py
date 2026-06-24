import streamlit as st
import requests
import pandas as pd
from src.charts import plot_top_popular, plot_price_vs_rating
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# URL da API hospedada no Railway
API_URL = os.getenv("API_URL", "https://steamanalyticsapi.up.railway.app")

st.set_page_config(page_title="Steam Analytics Dashboard", page_icon="🎮", layout="wide")

@st.cache_data(ttl=600)  # Mantém os filtros em cache por 10 minutos
def get_filter_options(api_url):
    try:
        response = requests.get(f"{api_url}/dashboard/filter-options", timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        st.error(f"Erro ao conectar com a API no endereço {api_url}: {e}")
    return None

filters = get_filter_options(API_URL)

if filters is not None:
    min_year = filters.get("min_year", 1997)
    max_year = filters.get("max_year", 2025)
    max_price = filters.get("max_price", 100.0)
    all_genres = filters.get("genres", [])
    
    st.title("Steam Analytics Dashboard")
    st.markdown("---")

    st.sidebar.header("Filtros do Dashboard")
    
    year_range = st.sidebar.slider("Ano de Lançamento", min_year, max_year, (2010, max_year))
    price_range = st.sidebar.slider("Faixa de Preço (US$)", 0.0, max_price, (0.0, 100.0 if max_price > 100 else max_price))
    selected_genres = st.sidebar.multiselect("Filtrar por Gêneros", all_genres, default=[])

    # Parâmetros de filtro para passar nas chamadas da API
    params = {
        "min_year": year_range[0],
        "max_year": year_range[1],
        "min_price": price_range[0],
        "max_price": price_range[1]
    }
    if selected_genres:
        params["genres"] = selected_genres

    # 1. Requisição das métricas principais do dashboard
    with st.spinner("Carregando métricas..."):
        try:
            metrics_resp = requests.get(f"{API_URL}/dashboard/metrics", params=params, timeout=10)
            metrics = metrics_resp.json() if metrics_resp.status_code == 200 else {"total_games": 0, "avg_price": 0.0, "avg_review_score": 0.0}
        except Exception:
            metrics = {"total_games": 0, "avg_price": 0.0, "avg_review_score": 0.0}

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Jogos", f"{metrics.get('total_games', 0):,}")
    with col2:
        st.metric("Preço Médio", f"US$ {metrics.get('avg_price', 0.0):.2f}")
    with col3:
        st.metric("Satisfação Média", f"{metrics.get('avg_review_score', 0.0):.1f}%")

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["Panorama Geral", "Análise de Preços", "Explorador de Dados"])

    # 2. Requisição para o gráfico de jogos populares
    with st.spinner("Carregando jogos populares..."):
        try:
            pop_resp = requests.get(f"{API_URL}/dashboard/popular-games", params=params, timeout=10)
            if pop_resp.status_code == 200:
                df_popular = pd.DataFrame(pop_resp.json())
            else:
                df_popular = pd.DataFrame(columns=['Name', 'Total_Reviews', 'Review_Score'])
        except Exception:
            df_popular = pd.DataFrame(columns=['Name', 'Total_Reviews', 'Review_Score'])

    # 3. Requisição do dataset para o gráfico de dispersão e tabela (limite de 5000 registros para performance)
    with st.spinner("Carregando explorador de dados..."):
        try:
            games_params = params.copy()
            games_params["limit"] = 5000
            games_resp = requests.get(f"{API_URL}/games", params=games_params, timeout=15)
            if games_resp.status_code == 200:
                df_games = pd.DataFrame(games_resp.json().get("games", []))
            else:
                df_games = pd.DataFrame(columns=['Name', 'Release date', 'Price', 'Total_Reviews', 'Review_Score', 'Main_Genre'])
        except Exception:
            df_games = pd.DataFrame(columns=['Name', 'Release date', 'Price', 'Total_Reviews', 'Review_Score', 'Main_Genre'])

    with tab1:
        if not df_popular.empty:
            st.plotly_chart(plot_top_popular(df_popular), width='stretch')
        else:
            st.warning("Nenhum dado retornado para gerar o gráfico de populares.")

    with tab2:
        if not df_games.empty:
            st.plotly_chart(plot_price_vs_rating(df_games), width='stretch')
            st.info("Dica: No gráfico acima, o tamanho dos círculos representa a popularidade total do jogo.")
        else:
            st.warning("Nenhum dado retornado para gerar a análise de preços.")

    with tab3:
        st.subheader("Visualização dos Dados Filtrados")
        if not df_games.empty:
            st.dataframe(
                df_games[['Name', 'Release date', 'Price', 'Total_Reviews', 'Review_Score', 'Main_Genre']],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("Nenhum registro encontrado para os filtros selecionados.")

else:
    st.error("Não foi possível carregar as opções de filtros da API.")
    st.info(f"Certifique-se de que a API no endereço {API_URL} está ativa e que as credenciais do banco foram configuradas corretamente no Railway.")
