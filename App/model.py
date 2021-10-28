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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def iniciarDatos():
    catalog = {'avist': None,
                'dateIndex': None
                }

    catalog['avist'] = lt.newList('SINGLE_LINKED', compare)
    catalog['dateIndex'] = om.newMap(omaptype='BST',
                                      comparefunction=compare)
    catalog['city']=om.newMap(omaptype='BST',
                                      comparefunction=compare)
    return catalog

# Funciones para agregar informacion al catalogo
def addAvist(catalog, avist):
    lt.addLast(catalog['avist'], avist)
    ciudad = avist['city']
    esta = om.contains(catalog['city'], ciudad)
    if not esta:
        listaCiudad = lt.newList()
        lt.addLast(listaCiudad, avist)
        om.put(catalog['city'], ciudad, listaCiudad)
    else:
        listaCiudad = om.get(catalog['city'], ciudad)['value']
        lt.addLast(listaCiudad, avist)
        om.put(catalog['city'], ciudad, listaCiudad)

# Requerimiento 1
def avistCiudad(catalog, ciudad):
    cantidadCiudades=0
    cantidadAvistCiudad=0
    listaciudad= lt.newList()
    for ciudad in lt.iterator(catalog['city']):
        cantidadCiudades+=1
        if catalog['city'] == ciudad:
            for linea in catalog['city']:
                cantidadAvistCiudad+= 1
                info =lt.newList()
                lt.addLast(info, linea['datetime'])
                lt.addLast(info, linea['city'])
                lt.addLast(info, linea['country'])
                lt.addLast(info, linea['duration (seconds)'])
                lt.addLast(info, linea['shape'])
                lt.addLast(listaciudad, info)
    return listaciudad

def listaFechas(listaciudad):
    listafechas= lt.newList()
    for linea in listaciudad:
        lt.addLast(listafechas, linea['datetime'])
    return listafechas

def ordenarlista(listafechas):
    listaOrdenada=sa.sort(listafechas, compare)
    return listaOrdenada

def ordenarArtistas(listaOrdenada, listaciudad):
    ordenada = lt.newList
    for fecha in listaOrdenada:
        for linea in listaciudad:
            if fecha == linea['datetime']:
                lt.addLast(ordenada, linea)
    return ordenada 

def primeros3(ordenada):
    primeros=lt.subList(ordenada, 1, 3)
    return primeros

def ultimos3(ordenada):
    ultimos=lt.subList(ordenada, (lt.size(ordenada))-2, 3)
    return ultimos
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de comparación
def compare(valor1, valor2):
    """
    Compara dos crimenes
    """
    if (valor1 == valor2):
        return 0
    elif valor1 > valor2:
        return 1
    else:
        return -1
