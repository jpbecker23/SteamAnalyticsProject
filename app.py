import streamlit as st

# Configuração da página
st.set_page_config(page_title="Steam Analytics Dashboard", page_icon="🎮", layout="wide")

# Título Principal
st.title("🎮 Steam Analytics Dashboard")
st.markdown("---")

# Sidebar para filtros futuros
st.sidebar.header("Filtros do Dashboard")
st.sidebar.info("Aguardando carregamento de dados...")

# KPI Cards (Placeholders)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Jogos", "0", "0%")
with col2:
    st.metric("Preço Médio", "R$ 0,00", "0%")
with col3:
    st.metric("Score de Avaliação Médio", "0", "0")

st.markdown("---")

# Gráficos (Base Inicial)
st.subheader("📊 Visualização Inicial")
st.info("Aguardando download dos dados para gerar análises.")

# Placeholder para os gráficos
col_g1, col_g2 = st.columns(2)
with col_g1:
    st.write("### Análise 1: Jogos Populares")
    st.warning("Pendente...")

with col_g2:
    st.write("### Análise 2: Preço vs Avaliação")
    st.warning("Pendente...")
