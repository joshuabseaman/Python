from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_recipe
from flask_app import DATABASE
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.confirm_password = data['confirm_password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password, confirm_password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(confirm_password)s);"
        results = connectToMySQL(DATABASE).query_db(query,data)
        return results

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for row in results:
            users.append( cls(row) )
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])


    @classmethod
    def update_one(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, password=%(password)s, confirm_password=%(confirm_password)s, updated_at=NOW() WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def delete_one(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate_registration(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!")
            is_valid=False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid=False
        if user['confirm_password'] != user['password']:
            flash("Passwords do not match")
            is_valid=False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        results = User.get_by_email(user)
        if not results:
            flash("Please register first.")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!")
            is_valid=False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid=False
        return is_valid

