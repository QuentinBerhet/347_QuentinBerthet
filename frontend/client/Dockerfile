# Utiliser l'image Node.js 14
FROM node:14

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . .

# Installer les dépendances
RUN npm install

# Construire l'application React
RUN npm run build

# Commande par défaut pour lancer l'application
CMD ["npm", "start"]
