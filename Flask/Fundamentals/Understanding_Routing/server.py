from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def hi_name(name):
    return f"Hello, {name}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ""
    for i in range(num):
        output += word
    return output

if __name__=="__main__":
    app.run(debug=True)