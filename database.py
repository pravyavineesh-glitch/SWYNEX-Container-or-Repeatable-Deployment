

import sqlite3
import os

def get_db_connection():

    os.makedirs("data", exist_ok=True)

    connection = sqlite3.connect("data/users.db")
    connection.row_factory = sqlite3.Row

    return connection


def create_user_table():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

