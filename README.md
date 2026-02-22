# 🎮 Pipeline ETL de Vendas de Videogames  
Transformação, análise e visualização de dados de vendas globais de videogames

## 📌 Visão Geral

Este projeto implementa um pipeline completo de **ETL (Extract, Transform, Load)** utilizando Python, PostgreSQL e Jupyter Notebook para analisar dados de vendas globais de videogames.  
O objetivo é demonstrar habilidades práticas em:

- Engenharia de dados  
- Limpeza e transformação de datasets  
- Criação de pipelines reprodutíveis  
- Visualização de dados  
- Integração com banco de dados relacional  
- Storytelling com dados  

O dataset utilizado contém informações sobre vendas por região, plataforma, gênero, publisher e ano de lançamento.

---

## 🧱 Arquitetura do Pipeline

📁 Fonte de Dados (CSV)
│
▼
🔍 Extração (Pandas)
│
▼
🧹 Transformação
- Limpeza de dados
- Tratamento de nulos
- Conversão de tipos
- Normalização de colunas
- Criação de novas métricas
│
▼
🗄️ Carga (PostgreSQL via SQLAlchemy)
│
▼
📊 Análises e Visualizações (Matplotlib / Seaborn)

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Ferramentas |
|----------|-------------|
| Linguagem | Python 3.11 |
| Banco de Dados | PostgreSQL |
| Conexão | SQLAlchemy |
| Manipulação de Dados | Pandas |
| Visualização | Matplotlib, Seaborn |
| Ambiente | Virtualenv + Jupyter Notebook |
| Versionamento | Git + GitHub |

---

## 📂 Estrutura de Pastas

Pipeline_Dados_Kaggle/
│
├── data/
│   └── videogame_sales.csv
│
├── notebooks/
│   └── etl_videogames.ipynb
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── utils.py
│pip install -r requirements.txt


├── .venv/
├── requirements.txt
├── README.md
└── .gitignore


---

## ▶️ Como Executar o Projeto

1. Clone o repositório

```bash
git clone https://github.com/fabioestevam2404/videogame-sales-etl.git
cd videogame-sales-etl

2. Crie e ative o ambiente virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

3. Instale as dependências
pip install -r requirements.txt

4. Configure as variáveis de ambiente
Crie um arquivo .env:
DB_HOST=localhost
DB_PORT=5432
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=videogames

5. Execute o notebook
jupyter notebook


📊 Exemplos de Visualizações
🔹 Vendas globais por gênero
<img width="1189" height="807" alt="image" src="https://github.com/user-attachments/assets/28aa3de0-5abb-49f2-aee4-90fa32925982" />

🔹 Top 10 jogos mais vendidos
<img width="1389" height="590" alt="image" src="https://github.com/user-attachments/assets/6a1bc0ab-46e5-4b5a-9aa4-57232d389ad7" />

🔹 Evolução das vendas ao longo dos anos
<img width="1389" height="989" alt="image" src="https://github.com/user-attachments/assets/23c488af-3a8a-4cf3-9c6c-9093010ee620" />

🧠 Insights Obtidos
Jogos de Ação e Esportes dominam as vendas globais.

A plataforma PS2 apresenta o maior volume histórico de vendas.

Publishers como Nintendo e Electronic Arts lideram o mercado.

O período entre 2005 e 2010 foi o auge da indústria em volume de vendas.


👨‍💻 Autor
Fabio Estevam  
Projeto de portfólio focado em Engenharia de Dados e Análise de Dados.
Sinta-se à vontade para contribuir ou enviar sugestões!







