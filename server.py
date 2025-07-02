# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/quote')
def get_quote():
    quote = random.choice(quotes)
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
