from flask import Blueprint, jsonify, request
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

