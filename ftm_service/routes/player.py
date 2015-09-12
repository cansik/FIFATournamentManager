import json
from flask import request
from app import pdb_query, pdb_data

__author__ = 'cansik'


def list():
    return ["player1", "player2"]


def create(player_id):
    post_data = request.json
    return "create"


def read(player_id):
    return "read"


def update(player_id):
    return "update"


def delete(player_id):
    return "delete"
