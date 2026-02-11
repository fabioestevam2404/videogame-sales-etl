"""
Script para carregar dados brutos na área de staging
"""

import pandas as pd
from src.database import DatabaseConnection


def load_raw_to_staging():
    """
    Carrega dados brutos do CSV para tabela staging
    """
    print("🔄 Iniciando carga para staging...")
    
    # Ler CSV
    df = pd.read_csv('./data/raw/vgsales.csv')
    
    print(f"📊 Linhas lidas: {len(df)}")
    print(f"📊 Colunas: {list(df.columns)}")
    
    # Conectar ao banco
    db = DatabaseConnection()
    engine = db.get_engine()
    
    # Carregar para staging
    df.to_sql(
        name='raw_sales',
        schema='staging',
        con=engine,
        if_exists='replace',  # Substitui se já existir
        index=False,
        method='multi'  # Carrega em lotes (mais rápido)
    )
    
    print("✅ Dados carregados em staging.raw_sales")
    
    # Exibir preview
    print("\n📋 Preview dos dados:")
    print(df.head())
    print(f"\n📈 Shape: {df.shape}")
    print(f"\n🔍 Tipos de dados:")
    print(df.dtypes)
    

if __name__ == "__main__":
    load_raw_to_staging()