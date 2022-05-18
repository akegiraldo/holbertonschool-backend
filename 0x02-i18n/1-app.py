#!/usr/bin/env python3
"""1. Basic Babel setup"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Class as config for the Flask app"""
    LANGUAGES = ["en", "fr"]
    default_locale = 'en'
    default_timezone = 'UTC'


app = Flask(__name__)
config = Config()
app.config.from_object(config)
babel = Babel(app)


@app.route('/')
def index():
    """
    Single / route and an index.html
    template that simply outputs
    “Welcome to Holberton” as page
    title (<title>) and “Hello world”
    as header (<h1>)
    """
    return render_template('1-index.html')
