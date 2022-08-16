from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        result = connectToMySQL('books_db').query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_db').query_db(query)
        authors = []
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        result = connectToMySQL('books_db').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data):
        query = "UPDATE authors SET name=%(name)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('books_db').query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM authors WHERE id = %(id)s;"
        return connectToMySQL('books_db').query_db(query, data)

    @classmethod
    def get_books_with_author( cls , data ):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_db').query_db( query , data )
        author = cls( results[0] )
        for row in results:
            book_data = {
                "id" : row["books.id"],
                "title" : row["title"],
                "num_of_pages" : row["num_of_pages"],
                "created_at" : row["books.created_at"],
                "updated_at" : row["books.updated_at"]
            }
            author.books.append( model_book.Book( book_data ) )
        return author