from flask import Blueprint, render_template, abort, request, jsonify
from flask_user import login_required

from src.models import GameOfLife

import os

bp = Blueprint('simulators', __name__, url_prefix='/simulators')


@bp.route('/')
@login_required
def home():
    return render_template('simulators/home.html')


@bp.route('/game-of-life')
@login_required
def game_of_life():
    return render_template('simulators/game_of_life.html')


@bp.route('/game-of-life/init', methods=['POST'])
def init_game_of_life():
    size = request.json['size']
    game = GameOfLife(size=size)
    game.random()
    return jsonify(game.board), 200


@bp.route('/game-of-life/evolve', methods=['POST'])
def evolve_game_of_life():
    size = request.json['size']
    board = request.json['board']
    board = [[board[i * size + j] for j in range(size)] for i in range(size)]
    game = GameOfLife(board=board)
    game.evolve()
    print(game.board)
    return jsonify(game.board), 200
