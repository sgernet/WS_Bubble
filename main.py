import os
from flask import Flask, request, jsonify

# Flask-App initialisieren
app = Flask(__name__)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)


# Home-Route
@app.route('/')
def home():
    return 'Hello Azure'

# Add-Route
@app.route('/add')
def add():
    # Zwei Zahlen aus den Query-Parametern lesen
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Bitte gültige Parameter a und b angeben.'}), 400

    # Summe berechnen
    result = a + b

    # Ergebnis als JSON zurückgeben
    return jsonify({'sum': result})

# Nur für lokalen Test
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
