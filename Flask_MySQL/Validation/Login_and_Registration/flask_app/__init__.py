from flask import Flask, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = "login and registration secret key"

bcrypt = Bcrypt(app)

DATABASE = "login_and_registration_db"