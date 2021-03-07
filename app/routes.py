from flask import render_template

from . import app
from .forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {
        'username': '007',
    }
    posts = [
        {
            'author': {'username':'kenny'},
            'body': 'Woohoo!!!',
        },
        {
            'author': {'username':'kyle'},
            'body': 'Dude, thats nice',
        },
    ]
    return render_template('index.html', title='home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()       # pass instance not class
    return render_template('login.html', title='login', form=form)