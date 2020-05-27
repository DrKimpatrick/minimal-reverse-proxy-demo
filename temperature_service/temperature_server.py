import random
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def get_temperature():
    temperature_c = random.randint(-10, 33)
    return { 'temperature_c': temperature_c }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')