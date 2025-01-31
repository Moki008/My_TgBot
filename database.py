import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            conn.execute("""
                CREATE TABLE IF NOT EXISTS dishes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(20),
                price FLOAT,
                about TEXT,
                category TEXT,
                portion TEXT,
                photo TEXT)
                        """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS review(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone_number TEXT,
                rate TEXT,
                comment TEXT
                )
            """)



    def save_review(self, data):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
            INSERT INTO review(name, phone_number, rate, comment)
            VALUES (?, ?, ?, ?)
            """,
                (data['name'], data['phone_number'], data['rate'], data['comment'])
            )

    def save_dishes(self, data):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
            INSERT INTO dishes(name, price, about,  category, portion ,photo)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
                (data['name'], data['price'], data['about'], data['category'], data['portion'], data['photo'])

      )
    def get_dishes(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = conn.execute("SELECT * FROM dishes")
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(row) for row in data]