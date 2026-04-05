# 🎮 Steam Analytics Dashboard

Projeto de análise de dados sobre jogos da plataforma Steam, utilizando dados reais para extrair insights sobre popularidade, precificação e avaliações.

## 🚀 Como Rodar o Projeto

1. **Clone o repositório** (ou baixe os arquivos).
2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Download dos Dados**:
   - Baixe `games.csv` de [Kaggle: Steam Games Dataset](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset).
   - Coloque o arquivo em `data/raw/`.
4. **Execute o Dashboard**:
   ```bash
   streamlit run app.py
   ```

## 📊 Funcionalidades (MVP)
- **Top 20 Jogos Populares**: Visualização interativa dos títulos com maior engajamento.
- **Relação Preço vs Avaliação**: Análise de como o custo impacta a percepção do usuário.

## 🛠️ Tecnologias
- **Python 3.14+**
- **Pandas** (Análise de Dados)
- **Plotly** (Visualizações Interativas)
- **Streamlit** (Dashboard Web)
