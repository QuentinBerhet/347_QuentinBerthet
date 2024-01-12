from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255), nullable=False)

# Initialise la base de données avec des données de test
@app.before_first_request
def before_first_request():
    db.create_all()
    if not Data.query.first():
        db.session.add(Data(value='Donnée 1'))
        db.session.add(Data(value='Donnée 2'))
        db.session.commit()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    data = Data.query.all()
    data_list = [{'id': item.id, 'value': item.value} for item in data]
    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
