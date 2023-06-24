from flask import Flask, render_template, request, jsonify
import MySQLdb
import request

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot
chatbot = ChatBot('HealthBot')

# Create a new trainer for the chat bot and train it on a corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

app = Flask(__name__)

INFERMEDICA_API_KEY = 'YOUR_API_KEY'
INFERMEDICA_APP_ID = 'YOUR_APP_ID'
# Configure MySQL connection
db = MySQLdb.connect(host='localhost', user='username', password='password', db='health_heroes_connect')
cursor = db.cursor()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    condition = request.form['condition']
    professional = request.form['professional']
    
    # Save user registration data to the database
    # Replace the following code with appropriate database queries
    cursor.execute("INSERT INTO users (name, age, gender, condition, professional) VALUES (%s, %s, %s, %s, %s)",
                   (name, age, gender, condition, professional))
    db.commit()
    
    return render_template('dashboard.html')

@app.route('/symptoms', methods=['POST'])
def check_symptoms():
    symptoms = request.form['symptoms']
    sex = request.form['sex']
    age = request.form['age']
    
    # Call the Infermedica API to analyze symptoms
    url = 'https://api.infermedica.com/v3/diagnosis'
    headers = {
        'Content-Type': 'application/json',
        'App-Key': INFERMEDICA_API_KEY,
        'App-Id': INFERMEDICA_APP_ID,
    }
    data = {
        'sex': sex,
        'age': age,
        'evidence': [{'id': symptom_id, 'choice_id': 'present'} for symptom_id in symptoms.split(',')],
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        treatment = result['conditions'][0]['treatments'][0]['name']
        return jsonify({'treatment': treatment})
    else:
        return jsonify({'error': 'An error occurred'})

@app.route('/discussion')
def discussion():
    return render_template('discussion.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    
    # Get the response from the chatbot
    response = chatbot.get_response(message)
    
    return jsonify({'message': str(response)})

if __name__ == '__main__':
    app.run()
