from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS so you can fetch from localhost

# Dummy users database (Replace with your own database)
users = {
    "sohaan": "1234",
    "alice": "4321",
    "bob": "0000"
}

# Home route for testing purpose
@app.route('/')
def home():
    return "<h1>Backend Running!</h1>"

# Route to verify username
@app.route('/verify-username', methods=['POST'])
def verify_username():
    data = request.json
    username = data.get('username')

    if username in users:
        return jsonify({'valid': True})
    else:
        return jsonify({'valid': False})

# Route to verify pin
@app.route('/verify-pin', methods=['POST'])
def verify_pin():
    data = request.json
    username = data.get('username')
    pin = data.get('pin')

    if users.get(username) == pin:
        return jsonify({'valid': True})
    else:
        return jsonify({'valid': False})

# Dashboard page after successful login
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Redirect after successful login (optional)
@app.route('/login-success')
def login_success():
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
