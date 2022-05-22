from flask import Flask
from umbrella import makeUmbrellaDecision
app = Flask(__name__)

@app.route('/')
def home():
    if makeUmbrellaDecision('new york', 'us'):
        return 'Bring an umbrella'
    else:
        return 'No need for an umbrella'