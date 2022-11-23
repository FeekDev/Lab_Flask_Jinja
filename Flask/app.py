# MODULOS
# SQlite3
import sqlite3
# FLASK
from flask import Flask, jsonify
# JSON
import json

# ASIGNACION DE OBJETO FLASK
app = Flask(__name__)

# VARIABLES GLOBALES
global proyectos
global usuarios
global diccionario_proyectos
proyectos = []
usuarios = []
diccionario_proyectos = {}


# CONEXION BASE DE DATOS
def conexion_Db():
    conexion = sqlite3.connect('sitio.db')
    cursor = conexion.cursor()
    return cursor


"""
OBTENCION DE USUARIO DE LA BASE DE DATOS
----------------------------------------
Se hara un JOIN para mostrar id del usuario, nombre del usuario
rol del usuario teniendo en cuenta la coincidencia
entre las tablas user, role y por ultimo la tabla
user_role_association_table que es quien posee las foreign key
"""


def consulta_usuarios():
    cursor = conexion_Db()
    consulta = cursor.execute(
        """SELECT
    user.id,
    user.username,
    role.name
    FROM user_role_association_table
    JOIN user
    ON user.id = user_role_association_table.user_id
    JOIN role
    ON role.id = user_role_association_table.role_id;
    """)
    usuarios = consulta.fetchall()
    return usuarios   # Retorna el arreglo de los usuarios

# RUTAS


# Ruta de bienvenida
@app.route('/')
def principal():
    mensaje = "Bienvenido, consulte con la URL: /proyecto/numeroID_de_proyecto"
    return str(mensaje)


"""
RUTA PARA OBTENER LOS PROYECTOS
-------------------------------
Tiene como objetivo consultar por id del proyecto
A medida que se ingresa el id, se va anexando ese proyecto
Al arreglo, de tal manera que la cantidad de id's
que se ingresen esa cantidad de proyectos se
guardaran en el arreglo
"""


@app.route('/proyecto/<int:id_proyecto>', methods=['GET'])
def proyecto(id_proyecto):
    with app.app_context():
        cursor = conexion_Db()
        usuarios = consulta_usuarios()
    cursor_proyectos = cursor.execute(
        'SELECT project_name FROM Project WHERE id=?', (id_proyecto,))
    mostrar_consulta = cursor_proyectos.fetchone()
    proyectos.append(mostrar_consulta)   # Aqui se anexa al arreglo
    diccionario = {
        "Projects": proyectos,
        "Users": usuarios
    }
    return json.dumps(diccionario, ensure_ascii= False, indent = 20)  # formato JSON

