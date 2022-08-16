from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_author

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        result = connectToMySQL('books_db').query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_db').query_db(query)
        books = []
        for row in results:
            books.append(cls(row))
        return books

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        result = connectToMySQL('books_db').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data):
        query = "UPDATE books SET title=%(title)s, num_of_pages=%(num_of_pages)s updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('books_db').query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM books WHERE id = %(id)s;"
        return connectToMySQL('books_db').query_db(query, data)

    @classmethod
    def get_author_with_books( cls , data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_db').query_db( query , data )
        book = cls( results[0] )
        for row in results:
            author_data = {
                "id" : row["authors.id"],
                "name" : row["name"],
                "created_at" : row["authors.created_at"],
                "updated_at" : row["authors.updated_at"]
            }
            book.authors.append( model_author.Author( author_data ) )
        return book