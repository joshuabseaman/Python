from flask import Flask, session

app = Flask(__name__)

app.secret_key = "dojo survey with validation secret key"