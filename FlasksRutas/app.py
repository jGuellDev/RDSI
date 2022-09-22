from flask import Flask, render_template, request

app = Flask(__name__)


# Endpoint - API
@app.route("/") # Ruta
def home(): # Funcion Manejadora
    return "Bienvenidos!!!"


# Endpoint - API
@app.route("/productos/") # Ruta
def productos(): # Funcion Manejadora
    return "Listado de productos"


######
if __name__ == '__main__':
    app.run(port=8000, debug=True)