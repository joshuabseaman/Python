from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_user
from flask_app import DATABASE

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_thirty, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_thirty)s, %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for row in results:
            recipes.append(cls(row))
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under_thirty=%(under_thirty)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_users_with_recipes(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for row in results:
            current_recipe = cls(row)
            user_data = {
                **row,
                "id" : row["users.id"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"]
            }
            current_user = model_user.User(user_data)
            current_recipe.user = (current_user)
            recipes.append(current_recipe)
        return recipes

    @classmethod
    def get_one_with_user(cls, data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        recipes = cls(results[0])
        for row in results:
            # current_recipe = cls(row)
            user_data = {
                **row,
                "id" : row["users.id"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"]
            }
            current_user = model_user.User(user_data)
            recipes.user = (current_user)
            # recipes.append(current_recipe)
        return recipes

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 1:
            flash("Name must not be blank.")
            is_valid = False
        if len(recipe['description']) < 1:
            flash("Description must not be blank.")
            is_valid = False
        if len(recipe['instructions']) < 1:
            flash("Instructions must not be blank.")
            is_valid = False
        if len(recipe['date_made']) < 1:
            flash("Date must not be blank.")
            is_valid = False
        return is_valid