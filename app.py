import os
import mysql.connector
import time

DB_HOST = os.getenv("MYSQL_HOST")
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DB")

def create_tables():
    """
    Fungsi ini terhubung ke database dan membuat semua tabel berdasarkan ERD.
    Terdapat logika retry untuk menunggu database siap.
    """
    conn = None
    max_retries = 10
    retry_delay = 5  
    
    for i in range(max_retries):
        try:
            print(f"Percobaan koneksi ke database... ({i+1}/{max_retries})")
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            print("Berhasil terhubung ke database!")
            cursor = conn.cursor()

            create_table_user_agent = """
            CREATE TABLE IF NOT EXISTS user_agent (
                user_admin_uuid VARCHAR(36) PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                hashed_password VARCHAR(255) NOT NULL,
                full_name VARCHAR(255) NOT NULL,
                phone_number VARCHAR(20),
                time_zone VARCHAR(50),
                role VARCHAR(50)
            )
            """
            create_table_user_client = """
            CREATE TABLE IF NOT EXISTS user_client (
                user_client_uuid VARCHAR(36) PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                hashed_password VARCHAR(255) NOT NULL,
                full_name VARCHAR(255) NOT NULL,
                phone_number VARCHAR(20),
                time_zone VARCHAR(50)
            )
            """
            create_table_tickets_details = """
            CREATE TABLE IF NOT EXISTS tickets_details (
                assets_details_id INT AUTO_INCREMENT PRIMARY KEY,
                issue_summary VARCHAR(255) NOT NULL,
                issue_details TEXT,
                subject VARCHAR(255) NOT NULL,
                department VARCHAR(255),
                user_admin_uuid VARCHAR(36),
                user_client_uuid VARCHAR(36),
                FOREIGN KEY (user_admin_uuid) REFERENCES user_agent(user_admin_uuid),
                FOREIGN KEY (user_client_uuid) REFERENCES user_client(user_client_uuid)
            )
            """
            create_table_tickets_status = """
            CREATE TABLE IF NOT EXISTS tickets_status (
                assets_status_id INT AUTO_INCREMENT PRIMARY KEY,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status VARCHAR(50),
                assets_details_id INT,
                FOREIGN KEY (assets_details_id) REFERENCES tickets_details(assets_details_id)
            )
            """
            create_table_help_topics = """
            CREATE TABLE IF NOT EXISTS help_topics (
                help_topics_id INT AUTO_INCREMENT PRIMARY KEY,
                help_description TEXT
            )
            """
            create_table_knowledgebase = """
            CREATE TABLE IF NOT EXISTS knowledgebase (
                knowledgebase_id INT AUTO_INCREMENT PRIMARY KEY,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                category VARCHAR(255),
                text TEXT,
                user_admin_uuid VARCHAR(36),
                help_topics_id INT,
                FOREIGN KEY (user_admin_uuid) REFERENCES user_agent(user_admin_uuid),
                FOREIGN KEY (help_topics_id) REFERENCES help_topics(help_topics_id)
            )
            """

            cursor.execute(create_table_user_agent)
            cursor.execute(create_table_user_client)
            cursor.execute(create_table_tickets_details)
            cursor.execute(create_table_tickets_status)
            cursor.execute(create_table_help_topics)
            cursor.execute(create_table_knowledgebase)
            
            print("Semua tabel berhasil dibuat atau sudah ada.")
            break  
            
        except mysql.connector.Error as err:
            print(f"Gagal koneksi: {err}")
            print(f"Menunggu {retry_delay} detik sebelum mencoba lagi...")
            time.sleep(retry_delay)
            
        finally:
            if conn and conn.is_connected():
                conn.close()

if __name__ == "__main__":
    create_tables()