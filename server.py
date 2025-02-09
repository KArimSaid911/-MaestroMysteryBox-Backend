from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # ✅ Enable CORS for all routes

# 🔐 Store used tokens in memory (consider using a database for production)
claimed_tokens = set()

@app.route('/check_token', methods=['GET'])
def check_token():
    """Check if a token has been claimed."""
    token = request.args.get('token')
    
    if not token:
        return jsonify({"error": "Missing token"}), 400

    return jsonify({"alreadyClaimed": token in claimed_tokens})

@app.route('/claim_token', methods=['POST'])
def claim_token():
    """Mark a token as claimed."""
    # ✅ Read token from both form-data and JSON body
    token = request.form.get('token') or request.json.get('token')

    if not token:
        return jsonify({"error": "Missing token"}), 400

    if token in claimed_tokens:
        return jsonify({"error": "Token already claimed"}), 403

    claimed_tokens.add(token)  # ✅ Mark token as used
    return jsonify({"status": "success", "message": "Token claimed"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
