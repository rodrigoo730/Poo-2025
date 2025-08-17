from manejaBeca import ManejaBeca
from manejaBeneficiario import ManejaBeneficiario

def test():
    manejaBeca=ManejaBeca()
    manejaBeneficiario=ManejaBeneficiario()
    manejaBeca.cargar()
    #manejaBeca.mostrar()
    manejaBeneficiario.cargar()
    return  manejaBeca,manejaBeneficiario