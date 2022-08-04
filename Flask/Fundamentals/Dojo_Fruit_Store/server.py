from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry_amt = request.form['strawberry']
    raspberry_amt = request.form['raspberry']
    apple_amt = request.form['apple']

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']

    count = int(strawberry_amt) + int(raspberry_amt) + int(apple_amt)
    print(f"Charging {first_name}{last_name} for {count} fruits.")

    now = datetime.now()

    return render_template("checkout.html", strawberry_amt=strawberry_amt, raspberry_amt=raspberry_amt, apple_amt=apple_amt, first_name=first_name, last_name=last_name, student_id=student_id, count=count, now=now)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    