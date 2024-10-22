#Develop by Oliveros, Opulencia, Pernecia

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

api_url = 'https://api.rinna.co.jp/models/scorer'

headers = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': '3acf3f2e3f3a4fdfb741ce5e314ffdfa'
}

@app.route('/')
def index():
    return render_template('session_based_scoring.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    dialog_history = data['dialogHistory']
    responses = data['responses']

    payload = {
        "dialogHistory": dialog_history,
        "responses": responses
    }

    response = requests.post(api_url, json=payload, headers=headers).json()

    top_candidate = response['topCandidate']
    scores = response['scores']

    return jsonify({
        'top_candidate': top_candidate,
        'score': scores[0]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5005)