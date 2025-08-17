import numpy as np
from paciente import paciente
import csv
class Maneja:
    __dimesion:int
    __cantidad:int
    __incremento:int
    __pacientes=np.ndarray
    def __init__(self,dimension=0):
        self.__cantidad=0
        self.__dimesion=dimension
        self.__incremento=5
        self.__pacientes=np.empty(dimension,dtype=paciente)

    def cargar(self):
        archivo=open('pacientes.csv')
        reader=csv.reader(archivo,delimiter=';')
        saltar=True
        for fila in reader:
            if saltar:
                saltar=False
            else:
                pacient=paciente(fila[0],fila[1],fila[2])
                self.agregar(pacient)

    def agregar(self,pacient):
        if self.__cantidad == self.__dimesion:
            self.__dimesion+=self.__incremento
            self.__pacientes.resize(self.__dimesion)
        else:
            self.__pacientes[self.__cantidad]=pacient
            self.__cantidad+=1

    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__pacientes[i].getNombre())

        