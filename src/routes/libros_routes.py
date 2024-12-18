from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from controller.libros_controllers import *

# Crea el Blueprint
libros = Blueprint('libros', __name__)


@libros.route('/getAll', methods=['GET'])
def getAllRoute():
    libros = getAll()
    return jsonify(libros), 200

@libros.route('/getById/<id>', methods=['GET'])
def getByIdRoute(id):
    libro = getById(id)
    if libro:
        return jsonify(libro), 200
    else:
        return jsonify({"error": "Libro no encontrado"}), 404

@libros.route('/insert', methods=['POST'])
@jwt_required()
def insertRoute():
    data = request.get_json()
    result = insert(data)
    if result:
        return jsonify({"message": "Libro insertado correctamente"}), 201
    else:
        return jsonify({"error": "Error al insertar el libro"}), 400
    
    
@libros.route('/delete/<id>', methods=['DELETE'])
@jwt_required()
def deleteRoute(id):
    result = delete(id)
    if result:
        return jsonify({"message": "Libro eliminado correctamente"}), 200
    else:
        return jsonify({"error": "Error al eliminar el libro"}), 400

@libros.route('/addReview/<id>', methods=['POST'])
@jwt_required()
def addReviewRoute(id):
    data = request.get_json()
    username = data.get('username')
    review = data.get('reseña')
    result = add_review(id, username, review)
    if result:
        return jsonify({"message": "Reseña agregada correctamente"}), 200
    else:
        return jsonify({"error": "Error al agregar la reseña"}), 400