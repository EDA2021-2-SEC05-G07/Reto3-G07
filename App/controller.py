"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def getIniciarDatos():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.iniciarDatos
    return catalog


# _________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# _________________

def getCargarDatos(catalog):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    UFOfile = cf.data_dir + 'UFOS-utf8-small.csv'
    input_file = csv.DictReader(open(UFOfile, encoding="utf-8"),
                                delimiter=",")
    for avist in input_file:
        model.addAvist(catalog, avist)
    return catalog
#req 1
def getAvisCiudad(catalog, ciudad):
    listaciudad = model.addAvist(catalog, ciudad)
    return listaciudad

def getListaFechas(listaciudad):
    listafechas= model.listaFechas(listaciudad)
    return listafechas

def getOrdenarLista(listafechas):
    listaOrdenada = model.ordenarlista(listafechas)
    return listaOrdenada

def getrdenarArtistas(listaOrdenada, listaciudad):
    ordenada = model.ordenarArtistas(listaOrdenada, listaciudad)
    return ordenada
def getprimeros3(ordenada):
    primeros = model.primeros3(ordenada)
    return primeros
def getultimos3(ordenada):
    ultimos = model.ultimos3(ordenada)
    return ultimos
# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
