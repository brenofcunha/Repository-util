from Estudo import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nova_rota')
def homepage():
    return render_template('homepage.html')
