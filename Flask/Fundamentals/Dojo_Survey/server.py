from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'dojo survey secret key'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user_info', methods=['post'])
def create_results():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['your_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show_results')

@app.route('/show_results')
def show_info():
    return render_template('results.html')

if __name__=="__main__":
    app.run(debug=True)