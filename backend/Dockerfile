# Utiliser l'image Python 3.9
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application (requirements.txt et tout le reste)
COPY requirements.txt requirements.txt
COPY . .

# Installer les dépendances
RUN pip install -r requirements.txt

# Commande par défaut pour lancer l'application
CMD ["python", "app.py"]
