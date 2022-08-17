from flask import Flask, session

app = Flask(__name__)

app.secret_key = "email validation with db secret key"