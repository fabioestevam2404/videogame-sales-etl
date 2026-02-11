"""
Módulo para gerenciar conexões com PostgreSQL
"""

import os
from dotenv import load_dotenv
import psycopg2

# Carregar variáveis de ambiente
load_dotenv()

class DatabaseConnection:
    """Classe para gerenciar conexões com o banco"""
    
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.database = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
    
    def get_engine(self):
        """
        Retorna engine SQLAlchemy para pandas
        """
        connection_string = (
            f"postgresql://{self.user}:{self.password}@"
            f"{self.host}:{self.port}/{self.database}"
        )
        return create_engine(connection_string)
    
    def get_connection(self):
        """
        Retorna conexão psycopg2 para SQL direto
        """
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
    
    def test_connection(self):
        """Testa conexão com o banco"""
        try:
            conn = self.get_connection()
            conn.close()
            print("✅ Conexão com banco de dados bem-sucedida!")
            return True
        except Exception as e:
            print(f"❌ Erro na conexão: {e}")
            return False

if __name__ == "__main__":
    db = DatabaseConnection()
    db.test_connection()