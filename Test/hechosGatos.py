#!/usr/bin/python3.8

# Modulos
# Jinja
from jinja2 import Environment, FileSystemLoader
# Request
from requests import get
from requests.exceptions import HTTPError
# JSON
import json
# Enlace de la API, se puede cambiar la page, ejemplo page=2,3,4...34
URL = 'https://catfact.ninja/facts?page=1'
"""
Manejo de excepciones
---------------------
Realiza todas las declaraciones en caso de mo fallar
"""
try:
    """
    Llamado a la API
    Key(cada hecho) : value(hecho del gato)
    """
    API = get(URL, json={'key': 'value'})
    # Conversion a JSON
    json_response = API.json()
    # Obtener el estado del llamado a la API
    API.raise_for_status()
    # Lista de echos
    coleccionHechos = []
    # Iteracion para obtener los echos
    for hechos in json_response['data']:
        coleccionHechos.append(hechos['fact'])

    # Obtener ruta de la plantilla HTML
    ruta_Archivo = FileSystemLoader('templates/')
    # Reconocimiento de ruta para plantilla
    env_var = Environment(loader=ruta_Archivo)
    # Obtencion de plantilla
    template = env_var.get_template('hechosGatos.txt')
    # Renderizacion
    salida = template.render(coleccionHechos=coleccionHechos)
    # Imprimir en la consola
    print(salida)
except HTTPError as errh:
    # Envia el mensaje de error en caso de fallar
    print("Http Error:", errh)
