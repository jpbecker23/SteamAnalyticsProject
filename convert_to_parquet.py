import pandas as pd
import os
import time

# Configurações
CSV_PATH = "data/raw/games.csv"
PARQUET_PATH = "data/raw/games.parquet"

def convert():
    if not os.path.exists(CSV_PATH):
        print(f"❌ Erro: O arquivo {CSV_PATH} não foi encontrado!")
        return

    print(f"⏳ Lendo CSV pesado ({os.path.getsize(CSV_PATH) / (1024*1024):.2f} MB)...")
    start_time = time.time()
    
    # Lendo o CSV (usando o fix das 40 colunas se necessário, mas para conversão simples o pandas costuma lidar bem se as aspas estiverem certas)
    df = pd.read_csv(CSV_PATH, low_memory=False)
    
    print(f"📦 Convertendo para Parquet...")
    df.to_parquet(PARQUET_PATH, compression='snappy', index=False)
    
    end_time = time.time()
    
    csv_size = os.path.getsize(CSV_PATH) / (1024*1024)
    pq_size = os.path.getsize(PARQUET_PATH) / (1024*1024)
    
    print("\n" + "="*30)
    print("✨ CONVERSÃO CONCLUÍDA! ✨")
    print(f"📄 CSV Original: {csv_size:.2f} MB")
    print(f"💎 Parquet Turbo: {pq_size:.2f} MB")
    print(f"📉 Redução de: {((1 - pq_size/csv_size) * 100):.1f}%")
    print(f"⏱️ Tempo gasto: {end_time - start_time:.2f} segundos")
    print("="*30)
    print(f"\n🚀 Agora o seu app vai ignorar o CSV e carregar o Parquet automaticamente!")

if __name__ == "__main__":
    convert()
