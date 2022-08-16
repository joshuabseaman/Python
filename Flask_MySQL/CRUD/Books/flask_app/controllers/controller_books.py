from flask import render_template, request, redirect
from flask_app import app
from flask_app.models import model_author
from flask_app.models import model_book


@app.route('/books')
def books():
    return render_template('books.html', books=model_book.Book.get_all())

@app.route('/book/create', methods=['post'])
def create_book():
    print(request.form)
    model_book.Book.save(request.form)
    return redirect('/books')

@app.route('/book/show/<int:id>')
def show_book(id):
    data = {
        "id": id
    }
    return render_template("show_book.html", books=model_book.Book.get_author_with_books(data))