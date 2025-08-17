
class atencion:
    __dni:int
    __fecha:str
    __importe:float

    def __init__(self,dni=0,fecha='',importe=0):
        self.__dni=dni
        self.__fecha=fecha
        self.__importe=importe

    def getDni(self):
        return self.__dni

    def getFecha(self):
        return self.__fecha

    def getImporte(self):
        return self.__importe
        
    