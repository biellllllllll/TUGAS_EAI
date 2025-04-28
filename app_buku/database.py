import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='perpustakaan'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None


