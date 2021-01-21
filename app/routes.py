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
    awards = open("Data/awards.txt",'r',encoding='utf-8')
    awards = awards.readlines()
    return render_template('awards.html',awards = awards)

@app.route('/books')
def books():
    books = open("Data/books.txt",'r',encoding='utf-8')
    books = books.readlines()
    return render_template('books.html',books = books)

@app.route('/journals')
def journals():

    journals = open("Data/journals.txt", "r", encoding="utf-8").readlines()

    return render_template('journals.html', journals = journals)

@app.route('/software')
def software():

    softwares = open("Data/software.txt", "r", encoding="utf-8").readlines()

    return render_template('software.html', softwares = softwares)

@app.route('/membership')
def membership():

    memberships = open("Data/membership.txt", "r", encoding="utf-8").readlines()

    return render_template('memberships.html', memberships = memberships)

@app.route('/workshop')
def workshop():

    workshops = open("Data/workshop.txt", "r", encoding="utf-8").readlines()

    return render_template('workshops.html', workshops = workshops)