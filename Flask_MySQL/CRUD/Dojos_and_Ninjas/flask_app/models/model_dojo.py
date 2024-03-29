from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_db').query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_db').query_db(query)
        dojos = []
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_db').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data):
        query = "UPDATE dojos SET name=%(name)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_db').query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_db').query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_db').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            if row["ninjas.id"]:
                ninja_data = {
                    "id" : row["ninjas.id"],
                    "first_name" : row["first_name"],
                    "last_name" : row["last_name"],
                    "age" : row["age"],
                    "created_at" : row["ninjas.created_at"],
                    "updated_at" : row["ninjas.updated_at"]
                }
                dojo.ninjas.append(model_ninja.Ninja(ninja_data))
        return dojo