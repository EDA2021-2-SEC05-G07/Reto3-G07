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
    catalog['datetime hora'] = om.newMap(omaptype='BST', 
                                        comparefunction=compare)
    catalog['datetime'] = om.newMap(omaptype='BST', 
                                        comparefunction=compare)
    catalog['duration (seconds)']=om.newMap(omaptype='BST',
                                      comparefunction=compare)
    catalog['longitude']=om.newMap(omaptype='BST',
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
    #indice para req 3
    datetim = datetime.datetime.strptime(avist['datetime'],"%Y-%m-%d %H:%M:%S")
    fecha = datetim.time()
    estaDatetime = om.contains(catalog['datetime hora'], fecha)
    if not estaDatetime:
        lstDatetime= lt.newList()
        lt.addLast(lstDatetime,avist)
        om.put(catalog['datetime hora'], fecha, lstDatetime)
    else: 
        lstDatetime = om.get(catalog['datetime hora'], fecha)['value']
        lt.addLast(lstDatetime, avist)
        om.put(catalog['datetime hora'], fecha, lstDatetime)
    #indice req 4 
    datetim = datetime.datetime.strptime(avist['datetime'],"%Y-%m-%d %H:%M:%S")
    fecha = datetim.date()
    estaDatetime = om.contains(catalog['datetime'], fecha)
    if not estaDatetime:
        lstDatetime= lt.newList()
        lt.addLast(lstDatetime,avist)
        om.put(catalog['datetime'], fecha, lstDatetime)
    else: 
        lstDatetime = om.get(catalog['datetime'], fecha)['value']
        lt.addLast(lstDatetime, avist)
        om.put(catalog['datetime'], fecha, lstDatetime)
    #indice duracion
    durationSec = float(avist['duration (seconds)'])
    dursec = om.contains(catalog['duration (seconds)'], durationSec)
    if not dursec:
        lstDurationSec= lt.newList()
        lt.addLast(lstDurationSec,avist)
        om.put(catalog['duration (seconds)'], durationSec, lstDurationSec)
    else: 
        lstDurationSec = om.get(catalog['duration (seconds)'], durationSec)['value']
        lt.addLast(lstDurationSec, avist)
        om.put(catalog['duration (seconds)'], durationSec, lstDurationSec)
    
    #indice longitud
    long = float(avist['longitude'])
    l = om.contains(catalog['longitude'], long)
    if not l:
        lstlong= lt.newList()
        lt.addLast(lstlong,avist)
        om.put(catalog['longitude'], long, lstlong)
    else: 
        lstlong = om.get(catalog['longitude'], long)['value']
        lt.addLast(lstlong, avist)
        om.put(catalog['longitude'], long, lstlong)

# Requerimiento 1
def AvistCiudad(catalog, ciudad):
    pareja = om.get(catalog['city'], ciudad)
    valor = me.getValue(pareja)
    listaOrdenada = sa.sort(valor, compareDates)
    size = lt.size(listaOrdenada)
    sizeAvist = lt.size(om.keySet(catalog['city']))
    return size, sizeAvist, listaOrdenada

def primeros3(ordenada):
    primeros=lt.subList(ordenada, 1, 3)
    return primeros

def ultimos3(ordenada):
    ultimos=lt.subList(ordenada, (lt.size(ordenada))-2, 3)
    return ultimos
#req 2
def duration(catalog, segmin, segmax):
    tiempos= om.values(catalog['duration (seconds)'], segmin, segmax)
    lst= lt.newList()
    for avist in lt.iterator(tiempos):
        for x in lt.iterator(avist):
            lt.addLast(lst, x)
    listaOrdenada = sa.sort(lst, compareDates)
    first= lt.subList(listaOrdenada, 1, 3)
    last=lt.subList(listaOrdenada, lt.size(listaOrdenada)-2, 3)
    return (listaOrdenada, first, last)

#req 3
def AvistHora(catalog, inferior, superior):
    inf = datetime.datetime.strptime(inferior,"%H:%M:%S")
    inf2 = inf.time()
    sup = datetime.datetime.strptime(superior,"%H:%M:%S")
    sup2 = sup.time()
    llaves_rango = om.keys(catalog['datetime hora'],inf2, sup2)
    lista = lt.newList()
    for hora in lt.iterator(llaves_rango):
        entry = om.get(catalog['datetime hora'], hora)
        valor = me.getValue(entry)
        for linea in lt.iterator(valor):
            lt.addLast(lista,linea)
    listaOrdenada = sa.sort(lista, compareDates)
    size = lt.size(listaOrdenada)
    return size, listaOrdenada
    
#Req 4
def avistRangoFechas(catalog, inferior, superior):
    inf = datetime.datetime.strptime(inferior,"%Y-%m-%d")
    inf2 = inf.date()
    sup = datetime.datetime.strptime(superior,"%Y-%m-%d")
    sup2 = sup.date()
    llaves_rango = om.keys(catalog['datetime'],inf2, sup2)
    lista = lt.newList()
    for fecha in lt.iterator(llaves_rango):
        entry = om.get(catalog['datetime'], fecha)
        valor = me.getValue(entry)
        for linea in lt.iterator(valor):
            lt.addLast(lista, linea)
    listaOrdenada = sa.sort(lista, compareDates)
    size = lt.size(listaOrdenada)
    return size, listaOrdenada
#req 5
def avistZona(catalog, longmin, longmax, latmin, latmax):
    zonas= lt.newList()
    avist= om.values(catalog['longitude'], longmin, longmax)
    for avistamientos in lt.iterator(avist):
        for avistamiento in lt.iterator(avistamientos):
            if float(avistamiento['latitude']) >= latmin and float(avistamiento['latitude']) <= latmax:
                lt.addLast(zonas, avistamiento)
    total= lt.size(zonas)
    first= lt.subList(zonas, 1, 3)
    last=lt.subList(zonas, total-2, 3)
    return (total, first, last)

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