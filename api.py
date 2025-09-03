# This is our own API Server for motivational quotes
# File: api.py

from flask import Flask, jsonify
import random

app = Flask(__name__)

# Our own database of English quotes
QUOTES_DATABASE = [
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Strive not to be a success, but rather to be of value.",
    "The mind is everything. What you think you become.",
    "Your time is limited, don't waste it living someone else's life.",
    "Winning isn’t everything, but wanting to win is.",
    "The only impossible journey is the one you never begin.",
    "Act as if what you do makes a difference. It does."
]

@app.route('/')
def home():
    return "Welcome to the Motivational Quotes API! Use the /quote endpoint to get a random quote."

@app.route('/quote')
def get_random_quote():
    # Select a random quote from our list
    random_quote = random.choice(QUOTES_DATABASE)
    
    # Return the quote in a structured JSON format
    return jsonify(
        quote=random_quote
    )

if __name__ == "__main__":
    # This part is for local testing. Render will use its own server (like Gunicorn).
    app.run(host='0.0.0.0', port=10000)
