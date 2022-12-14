class Auto:
    
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self.motor = Motor(cilindros = 4)

    def acelerar(self, tipo="despacio"):
        if tipo == 'rapida':
            self._motor.fuelInyection(10)
        else:
            self._motor.fuelInyection(3)

        self._estado = 'en_movimiento'

class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def fuelInyection(self, cantidad):
        pass
