import csv
from claseViajero import ViajeroFrecuente

class manejador:
    __lista = []
    def __init__(self):
        self.__lista= []
    def cargaArchivos(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo,delimiter=',')
        for comp in reader: 
                nuevoViajero = ViajeroFrecuente(int(comp[0]), comp[1], comp[2], comp[3], int(comp[4]))
                self.__lista.append(nuevoViajero)
        archivo.close()
    def mayor_millas(self):
        max = self.__lista[0]
        for i in range(len(self.__lista)):
            if (self.__lista[i] > max):
                max = self.__lista[i]
        print("el viajero con mas millas es: {}".format(max))
    def imprimir(self):
        for i in range(len(self.__lista)):
            print("{}".format(self.__lista[i]))
    def acumular(self):
        c = int(input("ingrese codigo de viajero para agregar millas"))
        v = 0
        for i in range(len(self.__lista)):
            if self.__lista[i].get_numeroViajero() == c:
                v = i
        num = int(input("ingrese cantidad de millas a agregar"))
        self.__lista[v] = self.__lista[v] + num
    def canjear(self):
        c = int(input("ingrese codigo de viajero para canjear millas"))
        v = 0
        for i in range(len(self.__lista)):
            if self.__lista[i].get_numeroViajero() == c:
                v = i
        num = int(input("ingrese cantidad de millas a canjear"))
        self.__lista[v] = self.__lista[v] - num