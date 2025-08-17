import csv
from beneficiario import Beneficiario
class ManejaBeneficiario:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def cargar(self):
        archivo=open('beneficiarios.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                beneficiario=Beneficiario(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],int(fila[6]),fila[7])
                self.__lista.append(beneficiario)
    
    def mostrarPorBeca(self,id):
        j=0
        for beneficiario in self.__lista:
            if int(beneficiario.getId()) == id:
                #print(beneficiario.getNombre(),' paso if')
                print(beneficiario.getDni(),'',beneficiario.getApellido())
                #print('paso d')
                j+=1
        return j
    
    def mostrarDni(self,dni):
        i=0
        encontrado=False
        while i<len(self.__lista) and not encontrado:
            if int(self.__lista[i].getDni()) == dni:
                encontrado=True
                if len(self.__lista[i].getId()) > 1:
                    print(self.__lista[i].getNombre(),' ',self.__lista[i].getDni())
                else:print('el beneficiario tiene una sola beca')
            i+=1
        if not encontrado:
            print('no se encontro el beneficiario ')
    
    def ordenar(self):
        self.__lista.sort()
        '''
        i=0
        while i<len(self.__lista)-1:
            if self.__lista[i].getFacultad() < self.__lista[i+1].getFacultad():
            
                self.__lista.sort()
            i+=1
        '''
    def mostrar(self):
        for bene in self.__lista:
            print(bene.getDni(),' ',bene.getApellido(),' ',bene.getFacultad())

    def mostrarPorProm(self):
        for bene in self.__lista:
            if int(bene.getPromedio()) >= 8 and len(bene.getId()) < 1 :
                print(bene.getNombre(),' ',bene.getApellido(),' ',bene.getPromedio())