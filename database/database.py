import sqlite3

DB_PATH = "data/resume_data.db"


def create_database():
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            skills TEXT,
            resume_score INTEGER,
            interview_score INTEGER
        )
    """)

    connection.commit()
    connection.close()


def save_data(name, skills, resume_score, interview_score):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users
        (name, skills, resume_score, interview_score)
        VALUES (?, ?, ?, ?)
    """, (name, skills, resume_score, interview_score))

    connection.commit()
    connection.close()


def get_all_data():

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()

    connection.close()

    return rows