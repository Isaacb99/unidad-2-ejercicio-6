
class ViajeroFrecuente:
    __num_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0
    def __init__(self,num=0,dni=None,nombre=None,apellido=None,millas=0):
        self.__num_viajero = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas
    def get_numeroViajero(self):
        return self.__num_viajero
    def __str__(self):
        return "{}   {}   {}   {}   {}".format(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
    def cantidadMillas(self):
        return (self.__millas_acum)
    def __gt__(self,otroViajero):
        return (self.__millas_acum > otroViajero.cantidadMillas())
    def __add__(self, n):
        return ViajeroFrecuente(self.__num_viajero, self.__dni,self.__nombre, self.__apellido, self.__millas_acum + n)
    def __sub__(self, n):
        return ViajeroFrecuente(self.__num_viajero, self.__dni,self.__nombre, self.__apellido, self.__millas_acum - n)