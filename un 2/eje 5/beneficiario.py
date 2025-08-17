class Beneficiario:
    __dni=0
    __nombre=''
    __apellido=''
    __carrera=''
    __facultad=''
    __anioCursa=0
    __promedio=0
    __idBecaAsignada=''

    def __init__(self,dni=0,nombre='',apellido='',carrera='',facultad='',anioCursa='',promedio=0,idBecaAsiganada=''):
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__carrera=carrera
        self.__facultad=facultad
        self.__anioCursa=anioCursa
        self.__promedio=promedio
        self.__idBecaAsignada=idBecaAsiganada

    def __str__(self):
        return print(self.__dni,self.__nombre,self.__apellido)

    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    
    def getCarrera(self):
        return self.__carrera
    def getFacultad(self):
        return self.__facultad
    
    def getAnioCursa(self):
        return self.__anioCursa
    def getPromedio(self):
        return self.__promedio
    def getId(self):
        return self.__idBecaAsignada
    
    def __lt__(self,otro):#ordena por facu y luego apellido
        
        resulta=False
        if self.__facultad == otro.getFacultad():
            resulta= self.__apellido < otro.getApellido()
        else:
            resulta= self.__facultad < otro.getFacultad()
        return resulta
        
        
        #return (self.__facultad,self.__apellido) < (otro.getFacultad(), otro.getApellido())