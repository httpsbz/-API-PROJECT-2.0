#Develop by Oliveros, Opulencia, Pernecia

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

api_url = 'https://api.rinna.co.jp/models/knowledge-generation'
headers = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': '3acf3f2e3f3a4fdfb741ce5e314ffdfa' 
}

@app.route('/')
def summary():
    return render_template('summary.html')

@app.route('/query', methods=['POST'])
def query():

    user_query = request.form['userQuery']

    data = {
        "query": user_query,
        "knowledge":  "The fastest land animal is the cheetah."
        "The Earth's atmosphere is composed of approximately 78% nitrogen, 21% oxygen, and 1% other gases."
        "The Great Wall of China is approximately 13,170 miles (21,196 kilometers) long."
        "The human brain contains approximately 86 billion neurons."
        "The Amazon Rainforest is home to a diverse range of plant and animal species."
        "The coldest temperature ever recorded on Earth was -128.6 degrees Fahrenheit (-89.2 degrees Celsius) in Antarctica."
        "The average lifespan of a housefly is between 15 to 30 days."
        "The tallest mountain in the world, Mount Everest, is approximately 29,032 feet (8,849 meters) tall."
        "The capital of Japan is Tokyo, which is one of the most populous cities in the world."
        "The Mona Lisa, painted by Leonardo da Vinci, is one of the most famous artworks in the world."
        "The speed of light in a vacuum is approximately 299,792 kilometers per second."
        "The largest ocean on Earth is the Pacific Ocean, covering approximately 63 million square miles (165 million square kilometers)."
        "The Eiffel Tower, located in Paris, France, was completed in 1889 and stands at a height of 1,063 feet (324 meters)."
        "The human body has 206 bones."
        "The circumference of the Earth at the equator is approximately 24,901 miles (40,075 kilometers)."
        "The first man to walk on the moon was Neil Armstrong, on July 20, 1969, during the Apollo 11 mission."
        "The chemical symbol for water is H2O, indicating that each water molecule consists of two hydrogen atoms and one oxygen atom."
        "The African elephant is the largest land animal, with males weighing up to 12,000 pounds (5,400 kilograms) and standing up to 13 feet (4 meters) tall."
        "The Pyramids of Giza, located in Egypt, are among the Seven Wonders of the Ancient World."
        "The human heart pumps approximately 2,000 gallons (7,571 liters) of blood each day."
        
    }

    response = requests.post(api_url, json=data, headers=headers).json()

    answer = response['response']
    keyword = response['keyword']

    return jsonify({'answer': answer, 'keyword': keyword})

if __name__ == '__main__':
    app.run(debug=True, port=5003)