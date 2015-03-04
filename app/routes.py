from flask import render_template as rendTemp
from app import app


@app.route('/')
@app.route('/index')
def index():
    return rendTemp('home.html', header='Benjamin (BJ) Johnson')

@app.route('/profile')
def profile():
    return rendTemp('profile.html', header='Profile')

@app.route('/portfolio')
def port():
    return rendTemp('portfolio.html', header='Portfolio')

@app.route('/certs')
def certs():
    return rendTemp('certs.html', header='Certifications')