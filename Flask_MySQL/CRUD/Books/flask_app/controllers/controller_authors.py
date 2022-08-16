from flask import render_template, request, redirect
from flask_app import app
from flask_app.models import model_author
from flask_app.models import model_book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template('authors.html', authors=model_author.Author.get_all())

@app.route('/author/create', methods=['post'])
def create_author():
    print(request.form)
    model_author.Author.save(request.form)
    return redirect('/authors')

@app.route('/author/show/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    return render_template("show_author.html", authors=model_author.Author.get_books_with_author(data))