from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '21dc6ebfa6175fda2e66a757eb1c10c8'


# Dont move this import above the database instance or it will cause circular import errors
from app import routes