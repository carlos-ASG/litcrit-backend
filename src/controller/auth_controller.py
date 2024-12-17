from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta
from db.db import db
from flask_cors import CORS  # Importar CORS

# Inicializar la app Flask
app = Flask(__name__)

# Configurar CORS para permitir solicitudes desde tu frontend
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})  # Permitir todas las rutas

# Ruta para autenticar el usuario (login)
@app.route('/login', methods=['POST', 'OPTIONS'])  # Asegurarse de incluir 'OPTIONS'
def authenticate(username,contra):
    try:
       # username = request.json.get('username')
        #password = request.json.get('contra')  # Asegúrate de que el nombre sea 'contra'

        user = db.users.find_one({"username": username})
        if user and check_password_hash(user['contra'], contra):
            access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": "Error en el servidor", "message": str(e)}), 500

# Ruta para registrar un nuevo usuario
@app.route('/register', methods=['POST', 'OPTIONS'])  # Asegurarse de incluir 'OPTIONS'
def register(username,contra):
    try:
        #username = request.json.get('username')
        #password = request.json.get('contra')  # Asegúrate de que el nombre sea 'contra'

        if db.users.find_one({"username": username}):
            return jsonify({"error": "Usuario ya existe"}), 400

        hashed_password = generate_password_hash(contra)
        db.users.insert_one({"username": username, "contra": hashed_password})
        return jsonify({"message": "Usuario registrado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": "Error en el servidor", "message": str(e)}), 500

# Ejecutar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
