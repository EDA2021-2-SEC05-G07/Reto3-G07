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


from DISClib.DataStructures.arraylist import addLast
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
    catalog['duration (hours/min)'] = om.newMap(omaptype='BST', 
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
    #añadir al indice para req 3
    durationHM = avist['duration (hours/min)']
    estaDuration = om.contains(catalog['duration (hours/min)'], durationHM)
    if not estaDuration:
        lstDurationHM= lt.newList()
        lt.addLast(lstDurationHM,avist)
        om.put(catalog['duration (hours/min)'], durationHM, lstDurationHM)
    else: 
        lstDurationHM = om.get(catalog['duration (hours/min)'], durationHM)['value']
        lt.addLast(lstDurationHM, avist)
        om.put(catalog['duration (hours/min)'], durationHM, lstDurationHM)


# Requerimiento 1
def ListaCiudad(catalog, ciudad):
    listaciudad= lt.newList()
    if ciudad in lt.iterator(om.keySet(catalog['city'])):
        for ciudad in lt.iterator(om.keySet(catalog['city'])):
            info =lt.newList()
            lt.addLast(info, ciudad['datetime'])
            lt.addLast(info, ciudad['city'])
            lt.addLast(info, ciudad['country'])
            lt.addLast(info, ciudad['duration (seconds)'])
            lt.addLast(info, ciudad['shape'])
            lt.addLast(listaciudad, info)
    return listaciudad
def avistCiudad2(catalog, ciudad):
    tamaño = lt.size(om.keySet(catalog['city']))
    entry = om.get(catalog['city'], ciudad)
    listaCiudad = lt.newList()
    lt.addLast(listaCiudad, me.getValue(entry))
    print(listaCiudad)
    listaOrdenada = sa.sort(listaCiudad, compareDates)
    print(listaOrdenada)
    return tamaño,listaOrdenada

def primeros3(ordenada):
    primeros=lt.subList(ordenada, 1, 3)
    return primeros

def ultimos3(ordenada):
    ultimos=lt.subList(ordenada, (lt.size(ordenada))-3, 3)
    return ultimos

#req 3
def durationHrs_min(catalog, maximum, minimun):
    lst_llaves= lt.newList()
    llaves_rango = om.keys(catalog['duration(hour/min)'],minimun, maximum)
    lt.addLast(lst_llaves, llaves_rango)
    listaOrdenada = sa.sort(lst_llaves, compareDates)
    #cambiar comparedates por el formato!!
    for avist in lst_llaves:
        info = lt.newList()
        lt.addLast(info, avist['datetime'])
        lt.addLast(info, avist['city'])
        lt.addLast(info, avist['country'])
        lt.addLast(info, avist['duration (seconds)'])
        lt.addLast(info, avist['shape'])
        pass 
#Req 4

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
def compareDates(ufo1, ufo2):
    date1= datetime.datetime.strptime(ufo1['datetime'],"%Y-%m-%d %H:%M:%S")
    date2= datetime.datetime.strptime(ufo2['datetime'],"%Y-%m-%d %H:%M:%S")
    fecha1 = date1.date()
    fecha2 = date2.date()
    return fecha1 < fecha2