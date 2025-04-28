from app_buku.database import get_db_connection

def fetch_all_books():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books

def fetch_book_by_id(book_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    conn.close()
    return book

def insert_book(title, author, category, year):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, category, year) VALUES (%s, %s, %s, %s)", (title, author, category, year))
    conn.commit()
    book_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return book_id

def update_book_info(book_id, title, author, category, year):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE books
        SET title = %s, author = %s, category = %s, year = %s
        WHERE id = %s
    """, (title, author, category, year, book_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_book_by_id(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()

class Buku:
    def __init__(self, id, judul, penulis, kategori, tahun):
        self.id = id
        self.judul = judul
        self.penulis = penulis
        self.kategori = kategori
        self.tahun = tahun
