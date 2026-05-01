import pandas as pd
import os
import time

# Configurações
CSV_PATH = "data/raw/games.csv"
PARQUET_PATH = "data/raw/games.parquet"

# Nomes CORRETOS das 40 colunas (o header original tem 39)
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

def convert():
    if not os.path.exists(CSV_PATH):
        print(f"Erro: O arquivo {CSV_PATH} não foi encontrado!")
        return

    print(f"Lendo CSV pesado ({os.path.getsize(CSV_PATH) / (1024*1024):.2f} MB) com correção de colunas...")
    start_time = time.time()
    
    df = pd.read_csv(CSV_PATH, header=0, names=CORRECT_COLUMNS, low_memory=False)
    
    print(f"Convertendo para Parquet...")
    df.to_parquet(PARQUET_PATH, compression='zstd', compression_level=6, index=False)
    
    end_time = time.time()
    
    csv_size = os.path.getsize(CSV_PATH) / (1024*1024)
    pq_size = os.path.getsize(PARQUET_PATH) / (1024*1024)
    
    print("\n" + "="*30)
    print("CONVERSÃO CONCLUÍDA!")
    print(f"CSV Original: {csv_size:.2f} MB")
    print(f"Parquet Turbo: {pq_size:.2f} MB")
    print(f"Redução de: {((1 - pq_size/csv_size) * 100):.1f}%")
    print(f"Tempo gasto: {end_time - start_time:.2f} segundos")
    print("="*30)
    print(f"\nAgora o seu app vai ignorar o CSV e carregar o Parquet automaticamente!")

if __name__ == "__main__":
    convert()
