import sqlite3

class DatabaseDish:
    def __init__(self, path):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            conn.execute("""
                CREATE TABLE IF NOT EXISTS dishes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price FLOAT,
                about TEXT)
                """)


