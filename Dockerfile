# легкий образ Python
FROM python:3.11-slim

# робоча директорія всередині контейнера
WORKDIR /app

# файл із залежностями та встановлення 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# копіюємо всі інші файли проєкту
COPY . .

# Команда для запуску нашого FastAPI сервера
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "10000"]