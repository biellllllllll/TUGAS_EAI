from app_peminjaman.database import get_db_connection

def fetch_all_loans():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM loans")
    loans = cursor.fetchall()
    cursor.close()
    conn.close()
    return loans

def fetch_loan_by_id(loan_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM loans WHERE id = %s", (loan_id,))
    loan = cursor.fetchone()
    cursor.close()
    conn.close()
    return loan

def insert_loan(user_id, book_id, tanggal_pinjam, tanggal_kembali, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO loans (user_id, book_id, tanggal_pinjam, tanggal_kembali, status) VALUES (%s, %s, %s, %s, %s)", (user_id, book_id, tanggal_pinjam, tanggal_kembali, status))
    conn.commit()
    loan_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return loan_id

def update_loan_info(loan_id, user_id, book_id, tanggal_pinjam, tanggal_kembali, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE loans
        SET user_id = %s, book_id = %s, tanggal_pinjam = %s, tanggal_kembali = %s, status = %s
        WHERE id = %s
    """, (user_id, book_id, tanggal_pinjam, tanggal_kembali, status, loan_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_loan_by_id(loan_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM loans WHERE id = %s", (loan_id,))
    conn.commit()
    cursor.close()
    conn.close()

class Peminjaman:
    def __init__(self, id, user_id, book_id, tanggal_pinjam, tanggal_kembali, status):
        self.id = id
        self.user_id = user_id
        self.book_id = book_id
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    

