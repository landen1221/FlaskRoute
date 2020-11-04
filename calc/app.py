# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

# print(operations.add(5,6))

@app.route('/add')
def addition():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"{operations.add(a,b)}"


@app.route('/sub')
def subtract():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"{operations.sub(a,b)}"

@app.route('/mult')
def multiply():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"{operations.mult(a,b)}"


@app.route('/div')
def divide():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"{operations.div(a, b)}"

@app.route('/math/<arg>')
def math(arg):
    a = int(request.args['a'])
    b = int(request.args['b'])


    if arg == 'add':
        return f"{operations.add(a,b)}"
    elif arg == 'sub':
        return f"{operations.sub(a, b)}"
    elif arg == 'mult':
        return f"{operations.mult(a, b)}"
    elif arg == 'div':
        return f"{operations.div(a, b)}"