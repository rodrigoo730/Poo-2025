
class Beca:
    __idBeca=0
    __tipo=''
    __importe=0

    def __init__(self,idBeca=0,tipo='',importe=0):
        self.__idBeca=idBeca
        self.__tipo=tipo
        self.__importe=importe

    def getIdBeca(self):
        return self.__idBeca
    
    def getTipo(self):
        return self.__tipo
    
    def getImporte(self):
        return self.__importe