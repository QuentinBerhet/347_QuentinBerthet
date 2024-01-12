from flask import Flask, jsonify
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# Désactiver la mise en cache pendant le développement
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# Configuration de la connexion MongoDB
if os.environ.get('FLASK_ENV') == 'development':
    app.config['MONGO_URI'] = 'mongodb://root:rootpassword@localhost:27017/dev_db'
elif os.environ.get('FLASK_ENV') == 'test':
    app.config['MONGO_URI'] = 'mongodb://root:rootpassword@localhost:27017/test_db'
else:
    # Configuration pour d'autres environnements (production, etc.)
    app.config['MONGO_URI'] = 'mongodb://username:password@localhost:27017/production_db'

mongo = PyMongo(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Récupérer les données depuis MongoDB
    data = list(mongo.db.items.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
