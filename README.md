# **Dokumentasi Proyek Akhir Basis Data**

---

### **Judul Proyek: Sistem Manajemen Basis Data Tiket Bantuan (IT Support Ticketing System)**

#### **Deskripsi Proyek**

Proyek ini adalah demonstrasi integrasi aplikasi **Python** dengan database **MySQL** dalam lingkungan **Docker** yang terisolasi. Tujuan utamanya adalah untuk mengimplementasikan skema basis data dari sebuah ERD yang telah dirancang, dan menjalankan berbagai operasi SQL (DDL & DML) untuk memenuhi tugas akhir mata kuliah Basis Data.

#### **Tech Stack & Tools**
* **Bahasa Pemrograman:** Python 3.9
* **Sistem Basis Data:** MySQL 8.0
* **Kontainerisasi:** Docker & Docker Compose
* **Pustaka Python:** `mysql-connector-python`

#### **Struktur Proyek**

### **Panduan Penggunaan Proyek (Demonstrasi UAS)**

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek secara keseluruhan.

1.  **Bersihkan Lingkungan Docker**
    Pastikan tidak ada kontainer lama atau data yang tersisa dengan perintah berikut:
    ```bash
    sudo docker compose down -v
    ```

2.  **Jalankan Seluruh Program UAS**
    Gunakan perintah ini untuk membangun image, menjalankan kontainer, dan mengeksekusi semua logika dalam `app.py` dari awal hingga akhir.
    ```bash
    sudo docker compose run --build app python3 /app/app.py
    ```

---

### **Jawaban Tugas UAS**

#### **1. Desain ERD**
*(Bagian ini dapat Anda jelaskan dengan menampilkan gambar ERD.)*
ERD ini terdiri dari 6 entitas utama yang saling berelasi: `user_agent`, `user_client`, `tickets_details`, `tickets_status`, `help_topics`, dan `knowledgebase`. Skema ini dirancang untuk mendukung sistem tiket bantuan.

#### **2. Implementasi Database dan Tabel**
-   **Tujuan:** Membuat semua tabel sesuai ERD dengan Primary Key dan Foreign Key.
-   **Metode:** Skrip `app.py` akan membuat semua tabel dengan perintah `CREATE TABLE IF NOT EXISTS`.

#### **3. Modifikasi Struktur Tabel**
-   **Tujuan:** Mengubah nama kolom `full_name` menjadi `user_name` pada tabel `user_agent`.
-   **Metode:** Perubahan ini sudah diterapkan langsung pada skrip `app.py` di dalam perintah `CREATE TABLE`.

#### **4. Input dan Tampilkan Data**
-   **Tujuan:** Mengisi data awal ke setiap tabel (minimal 10 baris).
-   **Metode:** Skrip `app.py` akan menjalankan beberapa perintah `INSERT INTO` untuk mengisi data ke setiap tabel.

#### **5. SELECT dengan Alias Kolom**
-   **Tujuan:** Menampilkan 2 kolom dengan alias.
-   **Contoh Query:**
    ```sql
    SELECT
        user_name AS Nama_Pengguna,
        email AS Email_Pengguna
    FROM user_agent;
    ```

#### **6. SELECT dengan WHERE dan Kondisi Jamak**
-   **Tujuan:** Menampilkan data dari tabel tertentu dengan 3 kondisi.
-   **Contoh Query:**
    ```sql
    SELECT
        td.issue_summary,
        td.department,
        ts.status
    FROM tickets_details AS td
    INNER JOIN tickets_status AS ts ON td.assets_details_id = ts.assets_details_id
    WHERE
        ts.created_date BETWEEN '2025-01-01' AND '2025-12-31'
        AND td.department = 'IT Support'
        AND ts.status = 'Open';
    ```

#### **7. INNER JOIN + WHERE (Soal Kasus)**
-   **Soal Kasus:** Tampilkan daftar tiket yang ditangani oleh **'Agent Satu'** yang statusnya **'Open'** dan dibuat pada tahun **2025**.
-   **Contoh Query:**
    ```sql
    SELECT
        ua.user_name,
        td.issue_summary,
        ts.status
    FROM
        user_agent AS ua
    INNER JOIN
        tickets_details AS td ON ua.user_admin_uuid = td.user_admin_uuid
    INNER JOIN
        tickets_status AS ts ON td.assets_details_id = ts.assets_details_id
    WHERE
        ua.user_name = 'Agent Satu'
        AND ts.status = 'Open'
        AND ts.created_date BETWEEN '2025-01-01' AND '2025-12-31';
    ```

#### **8. Fungsi**
-   **Tujuan:** Menggunakan fungsi `LIKE` dan `LIMIT`.
-   **Contoh Query:**
    ```sql
    SELECT
        full_name AS Nama_Klien,
        email AS Email_Klien
    FROM
        user_client
    WHERE
        full_name LIKE 'A%'
    LIMIT 4;
    ```

#### **9. Teori: Perbedaan WHERE dan HAVING**
-   **`WHERE`**: Filter baris **sebelum** dikelompokkan. Contoh: `SELECT * FROM tickets_details WHERE department = 'IT Support';`
-   **`HAVING`**: Filter kelompok **setelah** dikelompokkan. Contoh: `SELECT department, COUNT(*) FROM tickets_details GROUP BY department HAVING COUNT(*) > 1;`

#### **10. Integrasi Python + MySQL**
-   **Tujuan:** Menjalankan program Python yang terintegrasi dengan database.
-   **Metode:** Program `app.py` akan secara otomatis melakukan ini. Output dari `docker compose run` akan menampilkan hasil dari program Anda yang berhasil mengambil data dari database.

---

### **Lampiran Kode Program**

*(Anda bisa menempelkan kode lengkap untuk file `app.py`, `docker-compose.yml`, `Dockerfile`, dan `requirements.txt` di sini.)*
