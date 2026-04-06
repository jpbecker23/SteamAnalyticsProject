import plotly.express as px

def plot_top_popular(df):
    """
    Gera o gráfico de barras dos 20 jogos mais populares.
    """
    top_20 = df.nlargest(20, 'Total_Reviews').sort_values('Total_Reviews', ascending=True)
    
    fig = px.bar(
        top_20, 
        x='Total_Reviews', 
        y='Name', 
        orientation='h',
        color='Review_Score',
        color_continuous_scale='Viridis',
        text='Total_Reviews', 
        labels={'Total_Reviews': 'Total de Avaliações', 'Name': 'Nome do Jogo', 'Review_Score': 'Satisfação (%)'},
        template='plotly_dark',
        hover_data={
            'Name': False, 
            'Total_Reviews': ':,', 
            'Review_Score': ':.1f'
        }
    )
    
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(
        title="🔥 Top 20 Jogos Mais Populares",
        yaxis={'title': ''}, 
        margin=dict(l=200), 
        height=600,
        coloraxis_colorbar=dict(title="Score %")
    )
    return fig

def plot_price_vs_rating(df):
    """
    Gera o gráfico de dispersão Preço vs Avaliação.
    """
    df_sample = df.sample(min(5000, len(df))) if len(df) > 5000 else df
    
    fig = px.scatter(
        df_sample,
        x='Price',
        y='Review_Score',
        color='Price_Category',
        size='Total_Reviews',
        hover_name='Name',
        hover_data={'Price': ':.2f', 'Review_Score': ':.1f', 'Total_Reviews': ':,'},
        labels={'Price': 'Preço (US$)', 'Review_Score': 'Satisfação (%)', 'Price_Category': 'Categoria'},
        template='plotly_dark',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig.update_layout(
        title="💰 Relação Preço vs Avaliação (Amostra)",
        height=600
    )
    return fig
