#Rodrgo Pastran 39791772 19456
class Tramo:
    __cityOrigen:str
    __cityDestino:str
    __distancia:int
    __patente:str

    def __init__(self,origen='',destino='',dist=0,patente=''):
        self.__cityOrigen=origen
        self.__cityDestino=destino
        self.__distancia=dist
        self.__patente=patente
    
    def getOrigen(self):
        return self.__cityOrigen
    
    def getDestino(self):
        return self.__cityDestino
    
    def getDistancia(self):
        return self.__distancia
    
    def getPatente(self):
        return self.__patente
    
    def __gt__(self,other):
        return int(self.__distancia) > other