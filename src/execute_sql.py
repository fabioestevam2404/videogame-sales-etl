from src.database import DatabaseConnection

def execute_sql_file(filepath):
    conn = DatabaseConnection().get_connection()
    cursor = conn.cursor()

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            sql_content = file.read()

        # Divide comandos por ponto e vírgula
        commands = sql_content.split(";")

        for command in commands:
            clean = command.strip()
            if clean:  # Ignora comandos vazios
                cursor.execute(clean + ";")
                print(f"✔️ Comando executado:\n{clean[:60]}...")

        conn.commit()
        print("🎉 Todas as instruções SQL foram executadas com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao executar SQL: {e}")


    finally:
        cursor.close()
        conn.close()
        print("🔌 Conexão encerrada.")

if __name__ == "__main__":
    execute_sql_file("./sql/create_views.sql")
