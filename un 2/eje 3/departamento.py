
class departamento:
    __ident=int
    __nombre=str

    def __init__(self,ident=0,nombre=''):
        self.__ident=ident
        self.__nombre=nombre    

    def getNombre(self):
        return self.__nombre
    
    def getIdent(self):
        return int(self.__ident)