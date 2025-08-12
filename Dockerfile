# Menggunakan base image Python
FROM python:3.9-slim

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Menginstal semua pustaka yang dibutuhkan
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh isi direktori proyek ke dalam container
COPY . .

# Menjalankan aplikasi saat container dimulai
CMD ["python", "app.py"]