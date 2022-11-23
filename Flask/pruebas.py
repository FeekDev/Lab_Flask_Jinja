#!/usr/bin/python3
# Modulos
# SQlite3
import sqlite3
# Flask
from flask import Flask, jsonify


# Nombramiento aplicacion Flask
#app = Flask(__name__)

# Conexion base de datos
# def conexion_Db(cursor):
conexion = sqlite3.connect('sitio.db')
cursor = conexion.cursor()
# return cursor

# Ruta con identificador de proyecto
# @app.route('/proecto/', defaults={'id': 1})
# def proyectos():
cursor_usuarios = cursor.execute(
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
usuarios = {}
usuarios = cursor_usuarios.fetchall()
print(usuarios)
