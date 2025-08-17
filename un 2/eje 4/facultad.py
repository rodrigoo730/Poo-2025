
class facultad:
    __cod:int
    __nombre:str
    __direccion:str
    __localidad:str
    __telefono:int

    def __init__(self,codi=0,nom='',direccion='',localidad='',telefono=''):
        self.__cod=codi
        self.__nombre=nom
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
    
    def getCod(self):
        return self.__cod
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getLocal(self):
        return self.__localidad
    
    def getTelefono(self):
        return self.__telefono