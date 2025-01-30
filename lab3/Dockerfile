# Используем базовый образ Python
FROM python:3.9-slim

# Установка рабочей директории
WORKDIR /lab3

# Копирование зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Открытие порта для API
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "app.py"]