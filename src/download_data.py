"""
Script para download de dados do Kaggle
Dataset: Video Game Sales
"""

import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    """
    Baixa o dataset de vendas de videogames do Kaggle
    """
    # Inicializar API do Kaggle
    api = KaggleApi()
    api.authenticate()
    
    # Definir dataset
    dataset_name = "gregorut/videogamesales"
    download_path = "./data/raw"
    
    # Criar diretório se não existir
    os.makedirs(download_path, exist_ok=True)
    
    print(f"📥 Baixando dataset: {dataset_name}")
    
    # Baixar dataset
    api.dataset_download_files(
        dataset_name,
        path=download_path,
        unzip=True
    )
    
    print(f"✅ Dataset baixado em: {download_path}")

if __name__ == "__main__":
    download_dataset()