import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

class DatabaseConnection:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname=self.database
            )
            print("Conexão com banco de dados bem-sucedida!")
            return self.conn   # <-- ESSENCIAL
        except Exception as e:
            print(f"Erro ao conectar ao banco: {e}")
            raise  # <-- NÃO ENGOLIR O ERRO

    def get_connection(self):
        if self.conn is None:
            return self.connect()
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            print("Conexão encerrada.")

    def get_engine(self):
        url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        return create_engine(url)

 