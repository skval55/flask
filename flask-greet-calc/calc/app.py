# Put your app in here.

import operations
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add():
    """adds a and b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f'{operations.add(a,b)}'

@app.route('/sub')
def sub():
    """subtracts b from a"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f'{operations.sub(a,b)}'

@app.route('/mult')
def mult():
    """multiplys a and b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f'{operations.mult(a,b)}'

@app.route('/div')
def div():
    """divides b from a"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    print(a)
    return f'{operations.div(a,b)}'


# dictionary to hold the operations to refer to 
operators = {
    'add' : operations.add,
    'sub' : operations.sub,
    'mult' : operations.mult,
    'div' : operations.div
}

@app.route('/math/<operation>')
def operation(operation):
    """gets operation from operators dict then runs the operation"""
    print('operation ==',  operation)
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[operation](a,b)
    return str(result)
