from flask import jsonify, request
from controllers import create_item, get_item, update_item, delete_item

def init_routes(app):
    @app.route('/', methods=['GET'])
    def hola():
        
        return jsonify({"message": "Hola Mundo!"}), 200