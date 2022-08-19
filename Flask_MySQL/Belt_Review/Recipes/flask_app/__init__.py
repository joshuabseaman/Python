from flask import Flask, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = "recipes secret key"

bcrypt = Bcrypt(app)

DATABASE = "recipes_db"