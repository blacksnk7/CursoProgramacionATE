class Auto:
    def __init__(self, marca='Fiat', modelo='Duna', km='0'):
        self.marca = marca
        self.modelo = modelo
        self.km = km
        self.km_until_maintenance = 0

    def kilometraje(self):
        print(self.km)

    def recorrido(self, velocidad='0', distancia=''):
        if (self.km_until_maintenance >= 10000):
            print('Es necesario realizar el mantenimiento preventivo')
        self.km += distancia
        self.km_until_maintenance += distancia

    def realizar_mantenimiento(self):
        self.km_until_maintenance = 0

def test():
    '''Tests the functionallity of the object "Auto"'''
    auto1 = Auto('Ford', 'Ka', 5000)
    auto1.kilometraje()
    auto1.recorrido(100, 15000)
    auto1.kilometraje()
    auto1.recorrido(100, 1000)
    auto1.recorrido(100, 1000)
    auto1.realizar_mantenimiento()
    auto1.recorrido(100, 5000)
    auto1.recorrido(100, 5000)
    auto1.recorrido(100, 15000)
    auto1.kilometraje()

test()