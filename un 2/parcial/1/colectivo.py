
#Rodrgo Pastran 39791772 19456
class Colectivo:
    __patente:int
    __marca:str
    __modelo:str
    __capacidad:int
    __dniChofer:int
    __consumoProm=35
    
    def __init__(self,pantente=0,marca='',modelo='',capacidad=0,dni=0):
        self.__patente=pantente
        self.__marca=marca
        self.__modelo=modelo
        self.__capacidad=capacidad
        self.__dniChofer=dni
    
    def getConsumo(self):
        return self.__consumoProm

    def getPatente(self):
        return self.__patente
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getCapacidad(self):
        return self.__capacidad
    
    def getDniCho(sefl):
        return sefl.__dniChofer
    
    @classmethod
    def getConsumo(cls):
        return cls.__consumoProm
    