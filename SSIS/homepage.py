from flask import Blueprint, render_template

home = Blueprint('home', __name__)

# Home Page
@home.route('/')
@home.route('/HomePage')
def homepage():
    return render_template('homepage.html')