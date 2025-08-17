
class accidente:
    __accidentes=list

    def __init__(self):
        self.__accidentes=[]

    def inicializar(self):
        for i in range(19):
            self.__accidentes.append([])
            for j in range(12):
                self.__accidentes[i].append(0)
                
    
    def mostra(self):
        for i in range(len(self.__accidentes)):
            for j in range(len(self.__accidentes[i])):
                print('{}      '.format(self.__accidentes[i][j]),end='')
            print('\n')

    def cargar(self,depto,mes,accite):
        self.__accidentes[depto-1][mes-1]=accite

    def getAccte(self,depto,mes):
        return self.__accidentes[depto][mes]
    
    def getFila(self,iden):
        return self.__accidentes[iden]

    


    