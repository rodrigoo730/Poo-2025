
class Movilidad:
    __patente:str
    __tipo:str
    __capacidad:int
    __importeM:int
    __marca:str
    __modelo:str

    def __init__(self,patente='',tipo='',capac=0,impor=0,marca='',modelo=''):
        self.__patente=patente
        self.__tipo=tipo
        self.__capacidad=capac
        self.__importeM=impor
        self.__marca=marca
        self.__modelo=modelo

    def getPatente(self):
        return self.__patente
    
    def getTipo(self):
        return self.__tipo
    
    def getCapacidad(self):
        return self.__capacidad
    
    def getImportM(self):
        return self.__importeM
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def __str__(self):    ##ver
        return 'patente: '+self.__patente +'    tipo: '+self.__tipo+'    capacidad: '+ self.__capacidad+'    importe mensual: '+self.__importeM+'   marca: '+self.__modelo+'  modelo: '+self.__modelo
    
    '''
    @classmethod
    def getColegio(cls):
        return cls.colegio
    '''
   
        