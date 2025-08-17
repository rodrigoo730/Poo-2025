import csv
from paciente import paciente
class MPaciente:
    __pacientes=list

    def __init__(self):
        self.__pacientes=[]

    def cargar(self):
        archivo=open('pacientes.csv')
        reader=csv.reader(archivo,delimiter=';')
        salta=True
        for fila in reader:
            if salta:
                salta=False
            else:
                pacient=paciente(fila[0],fila[1],fila[2])
                self.agregar(pacient)

    def mostrar(self):
        for paciente in self.__pacientes:
            print(paciente.getUnidad(),' ',paciente.getNombre())

    def ordenar(self):
        self.__pacientes.sort()

    def agregar(self,pacie):
        self.__pacientes.append(pacie)

    def buscarPaciente(self,dni,ma):
        i=0
        encontrado=False
        while i<len(self.__pacientes) and not encontrado:
            #print(type(dni),' ',type(self.__pacientes[i].getDni()))
            if dni == int(self.__pacientes[i].getDni()):
                print('encontrado')
                encontrado=True
                cont=ma.buscarPorPac(dni)
                print('el paciente {} tuvo {} atenciones'.format(self.__pacientes[i].getNombre(),cont))
            i+=1

    def mostrarSin(self,ma):
        for paciente in self.__pacientes:
            if not ma.buscarDni(paciente.getDni()):
                print(paciente.getNombre(),' no tuvo atencion')
                

