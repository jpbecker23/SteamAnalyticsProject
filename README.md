# 🎮 Steam Analytics Dashboard

Um dashboard interativo de análise de dados sobre jogos da Steam, construído com **Python**, **Pandas**, **Plotly** e **Streamlit**. O projeto teve início com a análise direta de um dataset do **Kaggle** com mais de 170 mil jogos, transformando dados brutos em informações estruturadas e insights sobre popularidade, preços e satisfação dos usuários. Atualmente, esses dados são consumidos por meio de uma API REST, mantendo a aplicação focada na exploração e visualização dos resultados.

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
- **Requests**: Integração HTTP com o backend de dados.

## 🏗️ Arquitetura e Decisões
O projeto foi construído em duas etapas evolutivas que demonstram boas práticas de engenharia de dados:
### Fase 1: Limpeza e Otimização Local (Monólito)
* **Dataset Original:** Dados brutos do Kaggle cobrindo o catálogo da Steam.
* **Pipeline de Tratamento:** Limpeza de ruídos, tratamento de nulos em colunas essenciais, categorização de preços por faixa de mercado e cálculo dinâmico de score de review.
* **Compactação Parquet:** O dataset limpo foi convertido de CSV para **Parquet** usando compressão via PyArrow, reduzindo o tamanho em disco e acelerando a velocidade de leitura local no Pandas.
### Fase 2: Desacoplamento via API (Escalabilidade)
* Para otimizar a inicialização do app no Streamlit Cloud, a lógica de consulta e o banco de dados foram isolados em um repositório dedicado.
* Os dados tratados foram migrados para um banco PostgreSQL no Supabase, e o dashboard passou a se comunicar com a [SteamAnalyticsAPI](https://github.com/jpbecker23/SteamAnalyticsAPI) para recuperar apenas as fatias de dados já filtradas, deixando a interface leve e responsiva.

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

## ⚙️ Execução Local

1. Clone o repositório.
2. Crie um arquivo `.env` na raiz do projeto configurando a URL do backend de dados:
   ```env
   API_URL=https://steamanalyticsapi.up.railway.app
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicie o dashboard:
   ```bash
   streamlit run app.py
   ```

## ☁️ Deploy

Hospedado no **Streamlit Cloud** via GitHub.
---
Desenvolvido por **Joao Pedro Becker**.
