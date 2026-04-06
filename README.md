# 🎮 Steam Analytics Dashboard

Um dashboard interativo de análise de dados sobre jogos da Steam, construído com **Python**, **Pandas**, **Plotly** e **Streamlit**. Este projeto transforma um dataset do Kaggle (> 170k jogos) em insights visuais sobre popularidade, tendências de precificação e satisfação dos usuários.

> 🌐 **Acesse aqui**: [steamanalyticsproject.streamlit.app](https://steamanalyticsproject.streamlit.app/)

## 🚀 Funcionalidades Principais

- **Panorama de Popularidade**: Identificação dos jogos mais populares (através de Total Reviews) com filtros temporais.
- **Análise de Preços**: Estudo da relação entre preço de venda e pontuação de satisfação (%) dos usuários.
- **Explorador de Dados**: Ferramenta de filtragem dinâmica para buscar jogos específicos por gênero, ano e faixa de preço.

## 🛠️ Stack Tecnológico

- **Python 3.14+**
- **Streamlit**: Interface v2 e hospedagem.
- **Plotly Express**: Gráficos dinâmicos e interativos.
- **Pandas / PyArrow**: Processamento de dados e suporte a formatos binários (Parquet).

## 📊 Estrutura do Projeto

```text
SteamAnalyticsProject/
├── data/raw/               # Datasets (.parquet / .csv)
├── src/
│   ├── data_loader.py      # Carregamento com fallback Local/Remoto
│   ├── data_cleaner.py     # Limpeza resiliente de dados
│   └── charts.py           # Gráficos modulares
├── app.py                  # Ponto de entrada do Streamlit
├── requirements.txt        # Dependências
└── .env                    # Variáveis de ambiente
```

## ⚙️ Uso Local

1.  Clone o repositório.
2.  Crie a `venv` e instale o `requirements.txt`.
3.  Execute `streamlit run app.py`.

## ☁️ Deploy

Hospedado no **Streamlit Cloud** com CI/CD via GitHub. O carregamento de dados utiliza um **Google Drive ID** configurado nos *Secrets* da plataforma para evitar o limite de tamanho do Git.

---
Desenvolvido por **Joao Pedro Becker**.
