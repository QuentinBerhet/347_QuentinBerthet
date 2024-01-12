# Utilise une image légère pour le serveur web
FROM nginx:alpine

# Copie les fichiers du frontend dans le répertoire approprié
COPY ./frontend /usr/share/nginx/html

# Expose le port 8080
EXPOSE 8080

# Démarre le serveur nginx
CMD ["nginx", "-g", "daemon off;"]
