class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'la region {region} no es validad en {self.__pais}')

if __name__ == '__main__':
    casilla = CasillaDeVotacion(123, ['Bogota', 'Medellin'])
    print(casilla.region)
    casilla.region = 'Bogota'
    print(casilla.region)
    casilla.region = 'Cali'
    print(casilla.region)