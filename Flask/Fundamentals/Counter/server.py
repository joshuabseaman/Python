from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'counter secret key'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html')

@app.route('/counter')
def update_counter():
    session['counter'] +=1
    return redirect('/')

@app.route('/reset')
def reset_session():
    session.clear()
    return redirect('/')

@app.route('/add2')
def add_2():
    session['counter'] += 2
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)