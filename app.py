from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension



app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

# app.debug = True
# toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def home_page():
    '''Start page w/ button for initializing the game board'''
    return render_template('home.html')