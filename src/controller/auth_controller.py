# src/controller/auth_controllers.py
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta
from db.db import db

def authenticate(username, password):
    user = db.users.find_one({"username": username})
    if user and check_password_hash(user['contra'], password):
        access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
 
def register(username, password):
    if db.users.find_one({"username": username}):
        return jsonify({"error": "Usuario ya existe"}), 400

    hashed_password = generate_password_hash(password)
    db.users.insert_one({"username": username, "contra": hashed_password})
    return jsonify({"message": "Usuario registrado correctamente"}), 201

#usuario
# carlos
# 1234
