from flask import render_template, flash, redirect, url_for

from . import app
from .forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {
        "username": "007",
    }
    posts = [
        {"author": {"username": "kenny"}, "body": "Woohoo!!!",},
        {"author": {"username": "kyle"}, "body": "Dude, thats nice",},
    ]
    return render_template("index.html", title="home", user=user, posts=posts)


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()  # pass instance not class
    if form.validate_on_submit():
        flash(f'Login Requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template("login.html", title="login", form=form)
