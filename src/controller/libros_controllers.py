from bson.objectid import ObjectId
from db.db import db 


def getAll():
    libros = db.libros.find()
    resultado = []
    for libro in libros:
        libro['_id'] = str(libro['_id'])  # Convertir ObjectId a string
        libro['autor'] = str(libro['autor'])
        resultado.append(libro)
    print(resultado)
    return resultado

def getById(id):
    libro = db.libros.find_one({'_id': ObjectId(id)})
    if libro:
        libro['_id'] = str(libro['_id'])
        libro['autor'] = str(libro['autor'])
        return libro
    else:
        return None
