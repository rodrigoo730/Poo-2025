class Gastos:
    __patente:str
    __fecha:str
    __importe:float
    __descripcion:str

    def __init__(self,patente='',fecha='',importe=0,descripcion=''):
        self.__patente=patente
        self.__fecha=fecha
        self.__importe=importe
        self.__descripcion=descripcion

    def getPatente(self):
        return self.__patente
    
    def getFecha(self):
        return self.__fecha
    
    def getImporte(self):
        return self.__importe
    
    def getDescripcion(self):
        return self.__descripcion
    
    def __str__(self):
        return 'fecha: '+self.__fecha+'  patente:'+self.__patente
    
    def __lt__(self,other):
        if self.__fecha == other.getFecha():
            resultado=self.__patente < other.getPatente()
        else:
            resultado = self.__fecha < other.getFecha()
        return resultado