"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Req 1")
    print("3- Req 2")
    print("4- Req 3")
    print("5- Req 4")
    print("6- Req 5")

catalog = None

"""
Menu principal
"""
def initDatos():
    return controller.getIniciarDatos()

def cargarDatos(catalog):
    return controller.getCargarDatos(catalog)

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initDatos()
        cargarDatos(catalog)
    elif int(inputs[0]) == 2:
        ciudad = input("ingrese una ciudad para consultar avistamiento: ")
        size, sizeAvist, listaOrdenada  = controller.getAvistCiudad(catalog, ciudad)
        print("El total de avistamientos en " + str(ciudad)+ " es: " +str(size))
        print("El numero de ciudades con avistamientos es: " + str(sizeAvist))
        infoprim3 = lt.newList()
        prim3= controller.getprimeros3(listaOrdenada)
        for linea in lt.iterator(prim3):
            infolinea = lt.newList()
            lt.addLast(infolinea,(linea['datetime']))
            lt.addLast(infolinea,(linea['city']))
            lt.addLast(infolinea,(linea['country']))
            lt.addLast(infolinea,(linea['duration (seconds)']))
            lt.addLast(infolinea,(linea['shape']))
            lt.addLast(infoprim3, infolinea)
        print('###########################################################################################')
        print("los primeros 3 avistamientos dentro del rango son: " + str(infoprim3))
        print('###########################################################################################')
        ult3= controller.getultimos3(listaOrdenada)      
        for linea in lt.iterator(ult3):
            infolinea = lt.newList()
            lt.addLast(infolinea,(linea['datetime']))
            lt.addLast(infolinea,(linea['city']))
            lt.addLast(infolinea,(linea['country']))
            lt.addLast(infolinea,(linea['duration (seconds)']))
            lt.addLast(infolinea,(linea['shape']))
            lt.addLast(infoprim3, infolinea)
        print('#############################################################################################')
        print("los ultimos 3 avistamientos dentro del rango son: " + str(ult3))
        print('#############################################################################################')
    elif int(inputs[0]) == 3:
        segmin = float(input("Ingrese el límite inferior en segundos."))
        segmax = float(input("Ingrese el límite superior en segundos."))
        duration= controller.getduration(catalog, segmin, segmax)
        print("los primeros 3 avistamientos dentro del rango son: ")
        for linea in lt.iterator(duration[1]):
            print(linea['datetime'])
            print(linea['city'])
            print(linea['country'])
            print(linea['duration (seconds)'])
            print(linea['shape'])
        print("los ultimos 3 avistamientos dentro del rango son: ")
        for linea in lt.iterator(duration[2]):
            print(linea['datetime'])
            print(linea['city'])
            print(linea['country'])
            print(linea['duration (seconds)'])
            print(linea['shape'])
        total= lt.size(duration[0])
        print("El total de los avistamientos en el rango es: "+ str(total))
        pass
    elif int(inputs[0]) == 4:
        inferior = input("Ingrese el límite inferior en formato HH: MM.")
        superior = input("Ingrese el límite superior en formato HH: MM.")
        size, listaOrdenada = controller.getAvistHora(catalog, inferior, superior)
        print("El total de los avistamientos en el rango es: "+ str(size))
        infoprim3 = lt.newList()
        prim3= controller.getprimeros3(listaOrdenada)
        for linea in lt.iterator(prim3):
            infolinea = lt.newList()
            lt.addLast(infolinea,(linea['datetime']))
            lt.addLast(infolinea,(linea['city']))
            lt.addLast(infolinea,(linea['country']))
            lt.addLast(infolinea,(linea['duration (seconds)']))
            lt.addLast(infolinea,(linea['shape']))
            lt.addLast(infoprim3, infolinea)
        print('###########################################################################################')
        print("los primeros 3 avistamientos dentro del rango son: " + str(infoprim3))
        print('###########################################################################################')
        infoult3 = lt.newList()
        ult3= controller.getultimos3(listaOrdenada)      
        for linea in lt.iterator(ult3):
            infolinea = lt.newList()
            lt.addLast(infolinea,(linea['datetime']))
            lt.addLast(infolinea,(linea['city']))
            lt.addLast(infolinea,(linea['country']))
            lt.addLast(infolinea,(linea['duration (seconds)']))
            lt.addLast(infolinea,(linea['shape']))
            lt.addLast(infoprim3, infolinea)
        print('#############################################################################################')
        print("los ultimos 3 avistamientos dentro del rango son: " + str(ult3))
        print('#############################################################################################')
    elif int(inputs[0]) == 5:
        inferior = input("Ingrese el límite inferior en formato AAAA-MM-DD.")
        superior = input("Ingrese el límite superior en formato AAAA-MM-DD")
        size, listaOrdenada = controller.getavistRangoFechas(catalog, inferior, superior)
        print("El total de los avistamientos en el rango es: "+ str(size))
        infoprim3 = lt.newList()
        prim3= controller.getprimeros3(listaOrdenada)
        for linea in lt.iterator(prim3):
            infolinea = lt.newList()
            lt.addLast(infolinea,(linea['datetime']))
            lt.addLast(infolinea,(linea['city']))
            lt.addLast(infolinea,(linea['country']))
            lt.addLast(infolinea,(linea['duration (seconds)']))
            lt.addLast(infolinea,(linea['shape']))
            lt.addLast(infoprim3, infolinea)
        print('###########################################################################################')
        print("los primeros 3 avistamientos dentro del rango son: " + str(infoprim3))
        print('###########################################################################################')
        infoult3 = lt.newList()
        ult3= controller.getultimos3(listaOrdenada)      
        for linea in lt.iterator(ult3):
            infolinea = lt.newList()
            lt.addLast(infolinea,(linea['datetime']))
            lt.addLast(infolinea,(linea['city']))
            lt.addLast(infolinea,(linea['country']))
            lt.addLast(infolinea,(linea['duration (seconds)']))
            lt.addLast(infolinea,(linea['shape']))
            lt.addLast(infoprim3, infolinea)
        print('#############################################################################################')
        print("los ultimos 3 avistamientos dentro del rango son: " + str(ult3))
        print('#############################################################################################')
    elif int(inputs[0]) == 6:
        longmin = float(input("Ingrese la longitud minima."))
        longmax = float(input("Ingrese la longitud maxima."))
        latmin = float(input("Ingrese la latitud minima."))
        latmax = float(input("Ingrese latitud maxima."))
        zonas= controller.getavistZona(catalog, longmin, longmax, latmin, latmax)
        print("los primeros 3 avistamientos dentro del rango son: ")
        for linea in lt.iterator(zonas[1]):
            print('fecha: '+str(linea['datetime']))
            print('ciudad: '+str(linea['city']))
            print('pais: '+linea['country'])
            print('Duracion en segundos'+linea['duration (seconds)'])
            print('Forma: '+linea['shape'])
            latitud=round(float(linea['latitude']), 2)
            print('Latitud:' +str(latitud))
            longitud=round(float(linea['longitude']), 2)
            print('Longitud: ' +str(longitud))
        print("los ultimos 3 avistamientos dentro del rango son: ")
        for linea in lt.iterator(zonas[2]):
            print('fecha: '+str(linea['datetime']))
            print('ciudad: '+str(linea['city']))
            print('pais: '+linea['country'])
            print('Duracion en segundos'+linea['duration (seconds)'])
            print('Forma: '+linea['shape'])
            latitud=round(float(linea['latitude']), 2)
            print('Latitud:' +str(latitud))
            longitud=round(float(linea['longitude']), 2)
            print('Longitud: ' +str(longitud))
        total= zonas[0]
        print("El total de los avistamientos en el rango es: "+ str(total))
        pass
    else:
        sys.exit(0)
sys.exit(0)
