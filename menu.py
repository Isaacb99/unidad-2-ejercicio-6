from re import X
from tkinter import N
from manejadorViajero import manejador

class Menu:
    __op = 0
    def __init__(self,op = 0):
        self.__op = op
    def opciones (self):
        salir = True
        l=manejador()
        l.cargaArchivos()
        while salir:
            print("// MENU DE OPCIONES //")
            print("Opcion 1: ver el/los viajeros con mas millas acumuladas")
            print("Opcion 2: acumular millas")
            print("Opcion 3: canjear millas")
            print("Opcion 4: salir")
            self.__op = int(input('ingrese opcion a ejecutar'))
            if (self.__op== 1):
                l.mayor_millas()
            elif (self.__op== 2):
                l.imprimir()
                l.acumular()
                l.imprimir()
            elif (self.__op  == 3):
                l.imprimir()
                l.canjear()
                l.imprimir()
            else:
                salir = not salir
