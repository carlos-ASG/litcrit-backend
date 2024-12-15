from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

from routes.lirbos_routes import libros
from routes.autores_routes import autores

app.register_blueprint(libros, url_prefix='/libros')
app.register_blueprint(autores, url_prefix='/autores')

if __name__ == "__main__":
    app.run(debug=True)