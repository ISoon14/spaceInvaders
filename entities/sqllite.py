import sqlite3

class Sqllite:

    def __init__(self):
        self.conn = sqlite3.connect('bdd_invader.db')
        self.cursor = self.conn.cursor()

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
        dict = []
        result = self.cursor.execute("""SELECT nomJoueur, score FROM classement order by score desc limit 10 """)
        for element in result:
            dict.append({'name' : element[0],'score' : element[1]})
        return dict
