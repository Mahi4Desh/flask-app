from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello_world1")
def hello_world1():
    return "<h1>welcome to data science cojurse!</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h1>by pwskills!</h1>"
@app.route('/test')
def test():
    A = 5+6
    return "this function will run app {}".format(A)
@app.route('/test2')
def test2():
    data = request.args.get('x')
    return "this is data input from my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
    
