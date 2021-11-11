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
        tamaño, listaciudad = controller.getAvisCiudad2(catalog, ciudad)
        sizeLista= lt.size(listaciudad)
        print("El total de avistamientos en " + str(ciudad)+ " es: " +str(sizeLista))
        print("El numero de ciudades con avistamientos es: " + str(tamaño))
        ordenada = listaciudad
        primeros3= controller.getprimeros3(ordenada)
        print("La información de los primeros 3 avistamientos es: "+str(primeros3))
        ultimos3 = controller.getultimos3(ordenada)
        print("La información de los últimos 3 avistamientos es: "+str(ultimos3))
    elif int(inputs[0]) == 3:
        segmin = input("Ingrese el ímite inferior en segundos.")
        segmax = input("Ingrese el ímite inferior en segundos.")
        duration= controller.getduration(catalog, segmin, segmax)
        total= lt.size(duration[0])
        print("El total de los avistamientos en el rango es: "+ str(total))
        primeros= duration[1]
        print("los primeros 3 avistamientos dentro del rango son: " + str(primeros))
        ultimos= duration[2]
        print("los ultimos 3 avistamientos dentro del rango son: " + str(ultimos))
        pass
    elif int(inputs[0]) == 4:
        inferior = input("Ingrese el límite inferior en formato HH: MM.")
        superior = input("Ingrese el límite superior en formato HH: MM.")
        size, listaOrdenada = controller.getdurationHrs_min(catalog, inferior, superior)
        print("El total de los avistamientos en el rango es: "+ str(size))
        prim3= controller.getprimeros3(listaOrdenada)
        print("los primeros 3 avistamientos dentro del rango son: " + str(prim3))
        ult3= controller.getultimos3(listaOrdenada)
        print("los ultimos 3 avistamientos dentro del rango son: " + str(ult3))
    elif int(inputs[0]) == 5:
        inferior = input("Ingrese el ímite inferior en formato AAAA-MM-DD.")
        superior = input("Ingrese el límite superior en formato AAAA-MM-DD")
        size, listaOrdenada = controller.getavistRangoFechas(catalog, inferior, superior)
        print("El total de los avistamientos en el rango es: "+ str(size))
        prim3= controller.getprimeros3(listaOrdenada)
        print("los primeros 3 avistamientos dentro del rango son: " + str(prim3))
        ult3= controller.getultimos3(listaOrdenada)
        print("los ultimos 3 avistamientos dentro del rango son: " + str(ult3))
    elif int(inputs[0]) == 6:
        pass
    else:
        sys.exit(0)
sys.exit(0)
