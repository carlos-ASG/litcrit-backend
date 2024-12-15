from flask import Blueprint, jsonify
from controller.autores_controllers import *

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

