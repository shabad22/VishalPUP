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

@app.route('/copyright')
def copyright():

    copyrights = open("Data/copyright.txt", "r", encoding="utf-8").readlines()

    return render_template('copyright.html', copyrights = copyrights)


@app.route('/patent')
def patent():

    patents = open("Data/patent.txt", "r", encoding="utf-8").readlines()

    return render_template('patent.html', patents = patents)

@app.route('/mhrd')
def mhrd():

    mhrds = open("Data/mhrd.txt", "r", encoding="utf-8").readlines()

    return render_template('mhrd.html', mhrds = mhrds)

@app.route('/research')
def research():

    researchs = open("Data/research.txt", "r", encoding="utf-8").readlines()

    return render_template('research.html', researchs = researchs)

@app.route('/keynote')
def keynote():

    keynotes = open("Data/keynote.txt", "r", encoding="utf-8").readlines()

    return render_template('keynote.html', keynotes = keynotes)

@app.route('/resource')
def resource():

    resources = open("Data/resource.txt", "r", encoding="utf-8").readlines()

    return render_template('resource.html', resources = resources)

@app.route('/chaired')
def chaired():

    chaireds = open("Data/chaired.txt", "r", encoding="utf-8").readlines()

    return render_template('chaired.html', chaireds = chaireds)

@app.route('/trademark')
def trademark():

    trademarks = open("Data/trademark.txt", "r", encoding="utf-8").readlines()

    return render_template('trademark.html', trademarks = trademarks)

@app.route('/membership')
def membership():

    memberships = open("Data/membership.txt", "r", encoding="utf-8").readlines()

    return render_template('memberships.html', memberships = memberships)

@app.route('/workshop')
def workshop():

    workshops = open("Data/workshop.txt", "r", encoding="utf-8").readlines()

    return render_template('workshops.html', workshops = workshops)

@app.route('/conference')
def conference():

    international_conferences = open("Data/international_conferences.txt", "r", encoding="utf-8").readlines()
    national_conferences = open("Data/national_conferences.txt", "r", encoding="utf-8").readlines()

    return render_template('conferences.html', international_conferences = international_conferences, national_conferences = national_conferences)

@app.route('/project')
def project():

    mhrds = open("Data/mhrd.txt", "r", encoding="utf-8").readlines()
    researches = open("Data/researches.txt", "r", encoding="utf-8").readlines()

    return render_template('projects.html', mhrds = mhrds, researches = researches)