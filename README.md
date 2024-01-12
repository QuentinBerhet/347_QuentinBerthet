
# 347 projet

Ce projet est une application web simple construite avec Docker Compose, utilisant Flask pour le backend, MongoDB comme base de données, et React pour le frontend.

- backend : Contient les fichiers nécessaires pour le backend Flask.
- frontend : Contient les fichiers nécessaires pour le frontend React.

### Prérequis
- Docker installé sur votre machine

### Configuration
1. Créez un fichier .env.dev à la racine du projet avec les variables d'environnement pour le développement. Exemple :

```
FLASK_ENV=development
MONGO_URI=mongodb://root:rootpassword@localhost:27017/dev_db
```

2. Créez un fichier .env.test avec les variables d'environnement pour les tests.

### Utilisation

1. Ouvrez un terminal et placez-vous à la racine du projet.
2. Construisez et lancez les services pour l'environnement de développement :
```
docker-compose --env-file .env.dev up --build

```
pour Pour l'environnement de test : 
```
docker-compose --env-file .env.test up --build
```
3. Accédez à l'application :
* Backend : http://localhost:5000/api/data
* Frontend : http://localhost:3000

4. Pour arrêter les services, utilisez la combinaison de touches Ctrl+C dans le terminal.

### Personnalisation
* Personnalisez le code du backend dans le répertoire backend.
* Personnalisez le code du frontend dans le répertoire frontend/client.
* Ajoutez des dépendances, des fonctionnalités, et des tests selon vos besoins.


## Authors

- [@QuentinBerthet](https://github.com/BERTHETquentin)

