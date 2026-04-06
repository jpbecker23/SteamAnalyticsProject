# 🎮 Steam Analytics Dashboard

Um dashboard interativo de análise de dados sobre jogos da Steam, construído com **Python**, **Pandas**, **Plotly** e **Streamlit**. Este projeto transforma um dataset do Kaggle (> 170k jogos) em insights visuais sobre popularidade, tendências de precificação e satisfação dos usuários.

## 🚀 Funcionalidades Principais

- **Panorama de Popularidade**: Identificação dos jogos mais populares (através de Total Reviews) com filtros temporais.
- **Análise de Preços**: Estudo da relação entre preço de venda e pontuação de satisfação (%) dos usuários.
- **Explorador de Dados**: Ferramenta de filtragem dinâmica para buscar jogos específicos por gênero, ano e faixa de preço.
- **Tema Dark Premium**: Interface modernizada inspirada na estética gaming.

## 🛠️ Stack Tecnológico

- **Python 3.14+**
- **Streamlit**: Framework para o front-end v2 e hospedagem web.
- **Plotly Express**: Geração de gráficos interativos (zoom, hover, pan).
- **Pandas/NumPy**: Processamento e limpeza de dados (Data Wrangling).

## 📊 Estrutura do Projeto

```text
SteamAnalyticsProject/
├── data/
│   └── raw/                    # Dataset original (.csv)
├── notebooks/
│   └── 01_exploration.ipynb    # Análise exploratória inicial (EDA)
├── src/
│   ├── data_loader.py          # Carregamento e correção de colunas
│   ├── data_cleaner.py         # Limpeza e transformação (Data Wrangling)
│   └── charts.py               # Lógica modular de gráficos Plotly
├── app.py                      # Arquivo principal do Streamlit
└── requirements.txt            # Dependências do projeto
```

## ⚙️ Instalação e Uso Local

1.  **Clonar o Repositório**:
    ```bash
    git clone https://github.com/jpbecker23/SteamAnalyticsProject.git
    cd SteamAnalyticsProject
    ```

2.  **Configurar o Ambiente**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Baixar os Dados**:
    Baixe o dataset `games.csv` do Kaggle e coloque na pasta `data/raw/`.

4.  **Rodar o App**:
    ```bash
    streamlit run app.py
    ```

## ☁️ Deploy (Streamlit Cloud)

Este projeto foi desenhado para deploy direto via **GitHub** no **Streamlit Cloud**. 

> [!IMPORTANT]
> Certifique-se de que o arquivo `.gitignore` esteja configurado para não subir o arquivo `games.csv` (que ultrapassa 300MB), pois o GitHub tem limites de tamanho. O app local usará o arquivo local, mas para rodar em nuvem é necessário usar o Git LFS ou apontar para um storage externo.

---
Desenvolvido como projeto de portfólio para demonstração de habilidades em Data Science e Visualização.
