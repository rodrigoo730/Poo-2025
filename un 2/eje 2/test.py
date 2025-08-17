from tarjetaSube import tarjetaSube
from manejadorTarjeta import manejadorTarjeta
def test(manejador):
    for i in range(2):
        numero=int(input('ingrese numero de tarjeta: '))
        saldo=float(input('ingrese saldo de tarjeta: '))
        tarjeta=tarjetaSube(saldo,numero)
        #print(tarjeta)
        manejador.agregar(tarjeta)

    
    manejador.saldoNegativo()

    numTarjeta=int(input('ingrese numero tarjeta:'))
    saldo=manejador.buscarTarjeta(numTarjeta)
    if saldo!=None:
        print('el saldo de la tarjeta es{} '.format(saldo))
    else:print('no se encontro la tarjeta')
    


        