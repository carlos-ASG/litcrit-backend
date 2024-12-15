from bson.objectid import ObjectId
from db.db import db 


def getAll():
    autores = db.autores.find()
    resultado = []
    for autor in autores:
        autor['_id'] = str(autor['_id'])  # Convertir ObjectId a string
        resultado.append(autor)
    print(resultado)
    return resultado

def getById(id):
    autor = db.autores.find_one({'_id': ObjectId(id)})
    if autor:
        autor['_id'] = str(autor['_id'])
        return autor
    else:
        return None
