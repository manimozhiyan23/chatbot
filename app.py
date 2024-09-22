from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enables Cross-Origin requests (important for frontend communication)

# Define your intents dictionary
intents = {
    "intents": [
        {
            "student": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day"],
            "cre": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"]
        },
        {
            "student": ["Bye", "See you later", "Goodbye"],
            "cre": ["See you later, thanks for visiting", "Have a nice day", "Bye! Come back again soon."]
        },
        {
            "student": ["Thanks", "Thank you", "That's helpful"],
            "cre": ["Happy to help!", "Any time!", "My pleasure"]
        },
        {
            "student": ["How to join in workshop?", "How to apply the workshop?", "When and where is the workshop taking place?", "What are the registration requirements?", "How can I register for the workshop?", "How can I get more information or contact the organizers?"],
            "cre": ["We will guide you through a link so that you can follow and apply or call: 7358119288"]
        },
        {
            "student": ["Are there any additional fees or charges?", "Is there a payment deadline?", "Is there a minimum payment amount?", "Is there a registration fee?"],
            "cre": ["Free joining workshop"]
        },
        {
            "student": ["What time does the event start and end?", "Will there be reminders or notifications before the event?", "What is the time and date for the event?", "Is the timing flexible?", "When is the event/appointment/meeting scheduled?", "What are your hours today?"],
            "cre": ["We will be starting from 11am to 1pm"]
        },
        {
            "student": ["Will I be able to get the certificate after completing workshop?", "If any complaints or doubts"],
            "cre": ["Yes, you will be receiving the certificate but it will take some time"]
        },
        {
            "student": ["cre number", "If any complaints or doubts"],
            "cre": ["Kayal-7358119288", "Inba-7358114288"]
        }
    ]
}

# Function to handle user input and provide appropriate response
def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents['intents']:
        for pattern in intent['student']:
            if pattern.lower() in user_input:
                return random.choice(intent['cre'])
    return "Sorry, I'm not sure how to respond to that."

# API route for chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
