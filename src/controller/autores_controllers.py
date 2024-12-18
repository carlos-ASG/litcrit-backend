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

def insert(data):
    try:
        db.autores.insert_one(data)
        return True
    except Exception as e:
        print(f"Error al insertar el autor: {e}")
        return False

def delete(id):
    try:
        result = db.autores.delete_one({"_id": ObjectId(id)})
        return True if result.deleted_count == 1 else False
    except Exception as e:
        print(f"Error al eliminar el autor: {e}")
        return False

def add_book(id, id_libro):
    try:
        db.libros.update_one(
            {"_id": ObjectId(id)},
            {"$push": {"reseña": {"username": username, "reseña": review}}}
        )
        return True
    except Exception as e:
        print(f"Error al agregar la reseña: {e}")
        return False