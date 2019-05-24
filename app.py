from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello world"


@app.route('/hi')
def hi():
    return 'Hi!!!'

app.run()