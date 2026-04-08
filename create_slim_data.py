import pandas as pd
import os


INPUT_CSV = "data/raw/games.csv"
OUTPUT_SLIM = "data/raw/games_slim.parquet"

ESSENTIAL_COLUMNS = [
    'Name', 'Release date', 'Price', 'Positive', 'Negative', 'Genres'
]

CORRECT_COLUMNS = [
    'AppID', 'Name', 'Release date', 'Estimated owners', 'Peak CCU',
    'Required age', 'Price', 'Discount', 'DLC count', 
    'About the game', 'Supported languages', 'Full audio languages',
    'Reviews', 'Header image', 'Website', 'Support url', 'Support email',
    'Windows', 'Mac', 'Linux', 'Metacritic score', 'Metacritic url',
    'User score', 'Positive', 'Negative', 'Score rank', 'Achievements',
    'Recommendations', 'Notes', 'Average playtime forever',
    'Average playtime two weeks', 'Median playtime forever',
    'Median playtime two weeks', 'Developers', 'Publishers',
    'Categories', 'Genres', 'Tags', 'Screenshots', 'Movies'
]

def create_slim():
    if not os.path.exists(INPUT_CSV):
        print(f"Erro: {INPUT_CSV} not found.")
        return

    print(f"Lendo CSV pesado com correção de colunas...")
    df = pd.read_csv(INPUT_CSV, header=0, names=CORRECT_COLUMNS, low_memory=False)
    
    df_slim = df[['Name', 'Release date', 'Price', 'Positive', 'Negative', 'Genres']].copy()
    df_slim.rename(columns={'Genres': 'Main_Genre'}, inplace=True)
    
    print(f"Criando versão SLIM ({len(df_slim)} jogos)...")
    df_slim.to_parquet(OUTPUT_SLIM, compression='brotli', index=False)
    
    csv_size = os.path.getsize(INPUT_CSV) / (1024*1024)
    slim_size = os.path.getsize(OUTPUT_SLIM) / (1024*1024)
    
    print("\n" + "="*30)
    print("PERFORMANCE SLIM COMPLETA!")
    print(f"CSV Original: {csv_size:.2f} MB")
    print(f"Parquet Slim: {slim_size:.2f} MB")
    print(f"Redução de: {((1 - slim_size/csv_size) * 100):.1f}%")
    print("="*30)
    print(f"\nNOVO PASSO: Suba o arquivo '{OUTPUT_SLIM}' para o Drive e use o ID dele!")

if __name__ == "__main__":
    create_slim()
