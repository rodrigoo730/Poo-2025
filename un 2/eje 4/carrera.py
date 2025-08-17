
class carrera:
    __id:int
    __nombre:str
    __titulo:str
    __duracion:str
    __nivel:str
    __codFacultad:int

    def __init__(self,id=0,nomb='',titulo='',duracion='',nivel='',codFac=''):
        self.__id=id
        self.__nombre=nomb
        self.__titulo=titulo
        self.__duracion=duracion
        self.__nivel=nivel
        self.__codFacultad=codFac

    def getId(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def getNivel(self):
        return self.__nivel
    
    def getDuracion(self):
        return self.__duracion
    
    def getTitulo(self):
        return self.__titulo
    
    def getCodFacu(self):
        return self.__codFacultad
    

    def __lt__(self,otro):
        return self.__nombre < otro.getNombre()

        
    
        