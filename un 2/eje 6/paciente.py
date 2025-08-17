
class paciente:
    __dni:int
    __nombre:str
    __unidad:str

    def __init__(self,dni=0,nombre='',unidad=''):
        self.__dni=dni
        self.__nombre=nombre
        self.__unidad=unidad

    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getUnidad(self):
        return self.__unidad
    
    def __lt__(self,otro):
        if self.__unidad == otro.getUnidad():
            resultad= self.__nombre < otro.getNombre()
        else:
            resultad= self.__unidad < otro.getUnidad()
        return resultad