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

@app.route('/start-game', methods=['POST'])
def game_start():
    '''
    saves game board to session and redirects to gameboard page
    '''
    board = boggle_game.make_board()
    session['board'] = board
    session['responses'] = []

    return redirect('/game-board')

@app.route('/game-board')
def game_board():
    '''rendered game board'''
    board = session['board']

    return render_template('board.html', board= board)

@app.route('/guess', methods=['POST'])
def handle_guess():
    '''
    handle the guess
    '''

    answer = request.form['guess']
    
    responses = session['responses']
    responses.append(answer)
    session['responses'] = responses
    
    return redirect('/game-board')