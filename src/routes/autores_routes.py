from flask import Blueprint, jsonify,request
from flask_jwt_extended import jwt_required
from controller.autores_controllers import getAll,getById,insert,delete

# Crea el Blueprint
autores = Blueprint('autores', __name__)


@autores.route('/getAll', methods=['GET'])
def getAllRoute():
    autores = getAll()
    return jsonify(autores), 200

@autores.route('/getById/<id>', methods=['GET'])
def getByIdRoute(id):
    autor = getById(id)
    if autor:
        return jsonify(autor), 200
    else:
        return jsonify({"error": "Autor no encontrado"}), 404
    
@autores.route('/insert', methods=['POST'])
@jwt_required()
def insertRoute():
    data = request.get_json()
    result = insert(data)
    if result:
        return jsonify({"message": "Autor insertado correctamente"}), 201
    else:
        return jsonify({"error": "Error al insertar el autor"}), 400

@autores.route('/delete/<id>', methods=['DELETE'])
@jwt_required()
def deleteRoute(id):
    result = delete(id)
    if result:
        return jsonify({"message": "Autor eliminado correctamente"}), 200
    else:
        return jsonify({"error": "Error al eliminar el autor"}), 400

