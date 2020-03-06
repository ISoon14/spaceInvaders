import sqlite3

class Sqllite:

    def __init__(self):
        conn = sqlite3.connect('bdd_invader.db')
        cursor = conn.cursor()

    def reset_table(self):
        self.cursor.execute("""DROP TABLE Classement""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS classement(
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
             nomJoueur TEXT,
             score INT)
        """)
        self.conn.commit()

    def insert_data(self,nomJoueur, score):
        self.cursor.execute("""
        INSERT INTO classement(nomJoueur, score) VALUES(?, ?)""", (nomJoueur,score))
        self.conn.commit()

    def get_classement(self):
        result = self.cursor.execute("""SELECT nomJoueur, score FROM classement order by desc """)
        return self.cursor.fetchAll()
