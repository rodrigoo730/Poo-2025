
class tarjetaSube:
    __saldo:int
    __numero:int

    def __init__(self,saldo,numero):
        self.__saldo=saldo
        self.__numero=numero

    def getSaldo(self):
        return self.__saldo

    def getNumero(self):
        return self.__numero
    
    def __str__(self):
        return 'numero {} y saldo {} '.format(self.__numero,self.__saldo)

    def pagarPasaje(self,importe):
        if self.__saldo > importe:
            self.__saldo= self.__saldo-importe
        
            nuevoSaldo=self.__saldo
            print('operacion exitosa nuevo saldo: {}'.format(self.__saldo))
        else:
            nuevoSaldo=self.__saldo-importe
        return nuevoSaldo

    def cargarSaldo(self,saldo):
        if saldo > 0:
            print('el importe es positivo')
            self.__saldo=self.__saldo+saldo
        else: print('el importe es negativo: ')
        return
    
    def consultarSaldo(self):
        return 'el saldo es {}'.format(self.__saldo)
        
