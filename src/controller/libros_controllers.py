from bson.objectid import ObjectId
from db.db import db 


def getAll():
    libros = db.libros.find()
    resultado = []
    for libro in libros:
        libro['_id'] = str(libro['_id'])  # Convertir ObjectId a string
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

def insert(data):
    try:
        db.libros.insert_one(data)
        return True
    except Exception as e:
        print(f"Error al insertar el libro: {e}")
        return False

def delete(id):
    try:
        result = db.libros.delete_one({"_id": ObjectId(id)})
        return True if result.deleted_count == 1 else False
    except Exception as e:
        print(f"Error al eliminar el libro: {e}")
        return False

def add_review(id, username, review):
    try:
        db.libros.update_one(
            {"_id": ObjectId(id)},
            {"$push": {"reseña": {"username": username, "reseña": review}}}
        )
        return True
    except Exception as e:
        print(f"Error al agregar la reseña: {e}")
        return False