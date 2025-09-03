from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Data Standardization Project!'

if __name__ == '__main__':
    app.run(port=5000)