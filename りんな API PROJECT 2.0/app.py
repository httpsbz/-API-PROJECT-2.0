#Develop by Oliveros, Opulencia, Pernecia

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

api_url = 'https://api.rinna.co.jp/models/chitchat-generation'

headers = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': '3acf3f2e3f3a4fdfb741ce5e314ffdfa'
}

dialog_history = [
    "Hello! Good morning!", 
    "Hi! Good morning too!",  
    "How are you doing?", 
    "I'm doing fine. Thank you!" 
]

@app.route('/')
def index():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    global dialog_history

    userInput = request.form['userInput']

    if userInput.lower() == 'exit':
        dialog_history = []  
        return jsonify({'response': 'Conversation terminated.'})

    dialog_history.append(userInput)

    response = requests.post(api_url, json={'dialogHistory': dialog_history}, headers=headers).json()

    text = response['response']

    dialog_history.append(text)

    return jsonify({'response': text})

if __name__ == '__main__':
    app.run(debug=True, port=5001)