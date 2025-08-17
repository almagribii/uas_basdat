import os
import mysql.connector
import time
import datetime

DB_HOST = os.getenv("MYSQL_HOST")
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DB")

try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    print("Berhasil terhubung ke database!")
except mysql.connector.Error as err:
    print(f"Gagal terhubung ke database: {err}")
    print("Pastikan database berjalan dan detail koneksi sudah benar.")
    exit()

#  Fungsi untuk Operasi CRUD 

def tambah_user_agent():
    """Menambahkan data user_agent baru."""
    user_admin_uuid = input("UUID User Admin: ")
    email = input("Email: ")
    hashed_password = input("Hashed Password: ")
    full_name = input("Nama Lengkap: ")
    phone_number = input("Nomor Telepon: ")
    time_zone = input("Zona Waktu: ")
    role = input("Role: ")
    
    try:
        query = """
            INSERT INTO user_agent (user_admin_uuid, email, hashed_password, full_name, phone_number, time_zone, role)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_admin_uuid, email, hashed_password, full_name, phone_number, time_zone, role))
        conn.commit()
        print("Data user_agent berhasil ditambahkan.\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}\n")

def lihat_user_agent():
    """Menampilkan semua data dari tabel user_agent."""
    try:
        cursor.execute("SELECT * FROM user_agent")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()
    except mysql.connector.Error as err:
        print(f"Error: {err}\n")

def ubah_user_agent():
    """Mengubah data user_agent berdasarkan UUID."""
    user_admin_uuid = input("UUID user_agent yang ingin diubah: ")
    full_name = input("Nama Lengkap baru: ")
    email = input("Email baru: ")

    try:
        query = "UPDATE user_agent SET full_name=%s, email=%s WHERE user_admin_uuid=%s"
        cursor.execute(query, (full_name, email, user_admin_uuid))
        conn.commit()
        print("Data user_agent berhasil diubah.\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}\n")

def hapus_user_agent():
    """Menghapus data user_agent berdasarkan UUID."""
    user_admin_uuid = input("UUID user_agent yang ingin dihapus: ")
    try:
        cursor.execute("DELETE FROM user_agent WHERE user_admin_uuid=%s", (user_admin_uuid,))
        conn.commit()
        print("Data user_agent berhasil dihapus.\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}\n")

def lihat_tickets_dengan_user():
    """Menampilkan detail tiket beserta nama user_client dan user_agent (operasi JOIN)."""
    try:
        cursor.execute("""
            SELECT 
                td.assets_details_id, 
                td.issue_summary, 
                uc.full_name AS user_client_name, 
                ua.full_name AS user_admin_name
            FROM tickets_details td
            JOIN user_client uc ON td.user_client_uuid = uc.user_client_uuid
            LEFT JOIN user_agent ua ON td.user_admin_uuid = ua.user_admin_uuid
        """)
        for row in cursor.fetchall():
            print(row)
        print()
    except mysql.connector.Error as err:
        print(f"Error: {err}\n")


def menu():
    """Menampilkan menu interaktif untuk mengelola database."""
    while True:
        print("\n=== MENU HELP DESK ===")
        print("1. Tambah User Agent")
        print("2. Lihat Semua User Agent")
        print("3. Ubah Data User Agent")
        print("4. Hapus User Agent")
        print("5. Lihat Detail Tiket dengan Informasi User (JOIN)")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_user_agent()
        elif pilihan == "2":
            lihat_user_agent()
        elif pilihan == "3":
            ubah_user_agent()
        elif pilihan == "4":
            hapus_user_agent()
        elif pilihan == "5":
            lihat_tickets_dengan_user()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    menu()

if conn and conn.is_connected():
    cursor.close()
    conn.close()
    print("Koneksi database ditutup.")
