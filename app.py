from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenue dans le projet de Standardisation de Données!'

if __name__ == '__main__':
    app.run(port=5000)
