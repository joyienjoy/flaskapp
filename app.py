from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask & Docker'

@app.route('/one')
def one():
    return 'Hello from Flask & Docker - Page 1'

@app.route('/two')
def two():
    return 'Hello from Flask & Docker - Page 2'

@app.route('/one/first')
def onefirst():
    return 'Hello from Flask & Docker - Page 1 - Page 1st'
