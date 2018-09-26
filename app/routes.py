from app import app
from flask import request


# in order to provide numbers, the url must be given in this format:
# localhost:5000/(operator)?num1=x&num2=y
# if number not provided it will default to 0

@app.route('/')
@app.route('/add')
def add():
    num1 = request.args.get('num1', default=0, type=int)
    num2 = request.args.get('num2', default=0, type=int)
    return str(num1+num2)
@app.route('/subtract')
def subtract():
    num1 = request.args.get('num1', default=0, type=int)
    num2 = request.args.get('num2', default=0, type=int)
    return str(num1-num2)
@app.route('/multiply')
def multiply():
    num1 = request.args.get('num1', default=0, type=int)
    num2 = request.args.get('num2', default=0, type=int)
    return str(num1*num2)
@app.route('/divide')
def divide():
    num1 = request.args.get('num1', default=0, type=int)
    num2 = request.args.get('num2', default=0, type=int)
    return str(num1/num2)

