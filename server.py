from flask import Flask, request, jsonify
from flask_cors import CORS  # Added for cross-origin support

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dictionary to store claimed tokens
claimed_tokens = set()

@app.route('/check_token', methods=['GET'])
def check_token():
    token = request.args.get('token')
    
    if not token:
        return jsonify({"error": "Missing token"}), 400

    if token in claimed_tokens:
        return jsonify({"alreadyClaimed": True})
    else:
        return jsonify({"alreadyClaimed": False})

@app.route('/claim_token', methods=['POST'])
def claim_token():
    token = request.args.get('token')

    if not token:
        return jsonify({"error": "Missing token"}), 400

    claimed_tokens.add(token)  # Mark the token as used
    return jsonify({"status": "success", "message": "Token claimed"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000) 