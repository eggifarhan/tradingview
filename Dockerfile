# Gunakan Python versi stabil
FROM python:3.11-slim

# Set working directory di container
WORKDIR /app

# Copy semua file dari project lokal ke container
COPY . .

# Install dependencies dari requirements.txt (kalau ada)
RUN pip install --upgrade pip
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Jalankan file utama (ganti sesuai kebutuhan)
CMD ["python", "main.py"]
