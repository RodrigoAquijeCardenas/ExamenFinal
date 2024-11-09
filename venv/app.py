from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Función para conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect('alumnos.db')
    conn.row_factory = sqlite3.Row  # Esto permite acceder a las columnas por nombre en lugar de por índice
    return conn

@app.route('/')
def index():
    return "Base de datos levantada correctamente!"

if __name__ == '__main__':
    # Levanta el servidor de Flask
    app.run(debug=True)
