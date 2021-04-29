
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def home():
    return '<h1>APP clase 28/04/2021</h1><p>Mi primera aplicacion</p>'

app.run()