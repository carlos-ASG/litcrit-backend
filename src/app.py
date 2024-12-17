from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app)

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Cambia esto por una clave secreta segura
jwt = JWTManager(app)

from routes.libros_routes import libros
from routes.autores_routes import autores
from routes.auth_routes import auth

app.register_blueprint(libros, url_prefix='/libros')
app.register_blueprint(autores, url_prefix='/autores')
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True)