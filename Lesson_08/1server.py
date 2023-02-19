# flask basic app
# pip install flask
from flask import Flask

app = Flask(__name__) # create flask app


@app.route('/') # route to home page
def home1():
    return "Hello World"

@app.route('/home') # route to home page
def home():
    return "Hello World"


@app.route('/login') # route to home page
def login():
    return 'please log in'

def main():
    app.run(debug=True) # run flask app

main()