# Menggunakan image resmi Python sebagai base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Menyalin file `pyproject.toml` dan `poetry.lock`
COPY pyproject.toml poetry.lock /app/

# Menginstal Poetry
RUN pip install poetry

# Mengaktifkan virtual environment secara eksplisit
RUN poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project true

# Menginstal dependensi (termasuk Flask)
RUN poetry install --no-root

# Menyalin seluruh kode aplikasi ke dalam container
COPY . .

# Mengatur variabel environment untuk menjalankan Flask dari virtualenv
ENV PATH="/app/.venv/bin:$PATH"

# Menjalankan aplikasi Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
