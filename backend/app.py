from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'OK',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/api/acoes/<ticker>', methods=['GET'])
def obter_acao(ticker):
    return jsonify({
        'ticker': ticker,
        'preco': 100.50,
        'variacao': 2.5
    }), 200

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'API Online!'}), 200

if __name__ == '__main__':
    PORT = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
