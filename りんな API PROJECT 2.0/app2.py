#Develop by Oliveros, Opulencia, Pernecia

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_url = 'https://api.rinna.co.jp/models/ranker'

headers = {
    'Content-Type': 'application/json',
    'Cache-Control':'no-cache',
    'Ocp-Apim-Subscription-Key': '3acf3f2e3f3a4fdfb741ce5e314ffdfa'
}

@app.route('/')
def index():
    return render_template('input_form.html')

@app.route('/result', methods=['POST'])
def result():
    data = {
        "query": "",
        "candidates": [],
        "returnNum": 1
    }

    userInput = request.form['userInput']
    data['query'] = userInput

    candidate_replies = request.form.getlist('candidateReplies[]')
    data['candidates'] = candidate_replies

    response = requests.post(api_url, json=data, headers=headers)
    response_data = response.json()

    best_response = response_data['response']
    score = response_data['scores'][0]

    return render_template('result.html', userInput=userInput, bestResponse=best_response, score=score)

if __name__ == '__main__':
    app.run(debug=True, port=5002)