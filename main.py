from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    # Prüfen, ob JSON vorhanden ist
    if not request.is_json:
        return jsonify({'error': 'Bitte sende ein JSON mit dem Schlüssel "text".'}), 400

    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'Kein Text zur Analyse erhalten.'}), 400

    # Sentiment-Analyse mit TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Einteilung in Kategorien
    if polarity > 0.1:
        sentiment = 'Positiv'
    elif polarity < -0.1:
        sentiment = 'Negativ'
    else:
        sentiment = 'Neutral'

    return jsonify({'sentiment': sentiment, 'polarity': polarity})

if __name__ == '__main__':
    app.run(debug=True)
