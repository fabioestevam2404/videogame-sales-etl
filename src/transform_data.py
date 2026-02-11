"""
Script para transformar e limpar dados
"""

import pandas as pd
import numpy as np
from src.database import DatabaseConnection

def transform_data():
    """
    Aplica transformações e limpezas nos dados
    """
    print("🔄 Iniciando transformação dos dados...")
    
    db = DatabaseConnection()
    conn = db.get_connection()

    
    # Ler dados do staging
    df = pd.read_sql("SELECT * FROM staging.raw_sales", conn)

    
    print(f"📊 Registros originais: {len(df)}")
    
    # 1. Remover duplicatas
    df_clean = df.drop_duplicates()
    print(f"🧹 Após remover duplicatas: {len(df_clean)}")
    
    # 2. Tratar valores nulos
    # Year: preencher com mediana ou remover
    df_clean = df_clean.dropna(subset=['Year'])
    
    # Publisher: preencher com 'Unknown'
    df_clean['Publisher'] = df_clean['Publisher'].fillna('Unknown')
    
    print(f"🧹 Após tratar nulos: {len(df_clean)}")
    
    # 3. Conversões de tipo
    df_clean['Year'] = df_clean['Year'].astype(int)
    
    # 4. Criar colunas derivadas
    df_clean['Total_Sales'] = (
        df_clean['NA_Sales'] + 
        df_clean['EU_Sales'] + 
        df_clean['JP_Sales'] + 
        df_clean['Other_Sales']
    )
    
    # 5. Categorizar por década
    df_clean['Decade'] = (df_clean['Year'] // 10) * 10
    
    # 6. Categorizar vendas globais
    def categorize_sales(sales):
        if sales >= 10:
            return 'Blockbuster'
        elif sales >= 5:
            return 'Hit'
        elif sales >= 1:
            return 'Success'
        else:
            return 'Modest'
    
    df_clean['Sales_Category'] = df_clean['Global_Sales'].apply(categorize_sales)
    
    # 7. Criar ID único
    df_clean['game_id'] = range(1, len(df_clean) + 1)
    
    print(f"\n✅ Transformações aplicadas!")
    print(f"📊 Registros finais: {len(df_clean)}")
    print(f"📊 Novas colunas: Total_Sales, Decade, Sales_Category, game_id")
    
    return df_clean

def save_to_analytics(df):
    """
    Salva dados transformados no schema analytics
    """
    print("\n💾 Salvando no schema analytics...")
    
    db = DatabaseConnection()
    conn = db.get_connection()

    db = DatabaseConnection()
    engine = db.get_engine()

    df.to_sql(
        name='games_sales',
        schema='analytics',
        con=engine,
        if_exists='replace',
        index=False,
        method='multi'
    )
    
    print("✅ Dados salvos em analytics.games_sales")

if __name__ == "__main__":
    df_transformed = transform_data()
    save_to_analytics(df_transformed)
    
    # Salvar também como CSV processado
    df_transformed.to_csv('./data/processed/games_sales_clean.csv', index=False)
    print("✅ CSV limpo salvo em data/processed/")