from Database_Testing.database.db_connection import DatabaseConnection


def test_database_connection():
    db = DatabaseConnection()
    result = db.fetch_one("SELECT username, email FROM users WHERE id = %s", (1,))
    print(result)
    db.close()