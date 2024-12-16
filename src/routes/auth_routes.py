# src/routes/auth_routes.py
from flask import Blueprint, request
from controller.auth_controller import authenticate,register

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('contra')
    return authenticate(username, password)

@auth.route('/register', methods=['POST'])
def register_route():
    data = request.get_json()
    username = data.get('username')
    password = data.get('contra')
    return register(username, password)