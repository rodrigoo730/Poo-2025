from tarjetaSube import tarjetaSube
def test():
    for i in range(1):
        numero=int(input('ingrese numero de tarjeta: '))
        saldo=float(input('ingrese saldo de tarjeta: '))
        tarjeta=tarjetaSube(saldo,numero)
        print(tarjeta)

    print('prueba de tarjeta: {} metodos :'.format(tarjeta))
    saldoCargar=float(input('ingrese monto a pagar: '))
    if tarjeta.pagarPasaje(saldoCargar) < 0:
        print('no se realizo el pago ')
    cargarSaldo=float(input('ingrese saldo a cargar: '))
    tarjeta.cargarSaldo(cargarSaldo)


        