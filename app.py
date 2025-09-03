from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Data Standardization Project v1.1!'

if __name__ == '__main__':
    app.run(port=5000)