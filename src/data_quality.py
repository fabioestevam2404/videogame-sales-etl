from src.database import DatabaseConnection

def run_quality_checks():
    db = DatabaseConnection()
    conn = db.get_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM staging_table")
    result = cursor.fetchone()

    print(f"Total de registros na staging: {result[0]}")

    cursor.close()
    db.close()

if __name__ == "__main__":
    run_quality_checks()

