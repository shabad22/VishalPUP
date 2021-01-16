from flask import render_template
from app import app


@app.route('/')
def index():
    """
    This route is for the home page
    """
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')