from tarjetaSube import tarjetaSube
class manejadorTarjeta:
    __list=list

    def __init__(self,list=[]):
        self.__list=list

    def agregar(self,tarjeta):
        if type(tarjeta) is tarjetaSube:
            self.__list.append(tarjeta)
            print('tarjeta se agrego correctamente')
        else:print('tarjeta no es del tipo tarjetaSube')


    def saldoNegativo(self):
        for tarjeta in self.__list:
            if tarjeta.getSaldo() < 0:
                print('el numero de la tarjeta sube con saldo negativo es {}'.format(tarjeta.getNumero()))

    def buscarTarjeta(self,num):
        i=0
        saldo=None
        bandera=False
        while i<len(self.__list) and not bandera:
            #print('paso while y numero es {}'.format(self.__list[i].getNumero()))
            if (self.__list[i].getNumero()==num):
                saldo=self.__list[i].getSaldo()
                bandera=True
            i+=1
        return saldo
    
    def mostrar(self):
        i=0
        while i<len(self.__list):
            print(self.__list[i])
            i+=1