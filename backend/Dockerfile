# Utilise une image légère de Python
FROM python:3.8-slim

# Définis le répertoire de travail
WORKDIR /app

# Copie les fichiers requis
COPY ./backend/requirements.txt /app/
COPY ./backend/app.py /app/
COPY ./backend/templates /app/templates

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port 5000
EXPOSE 5000

# Démarre l'application
CMD ["python", "app.py"]
