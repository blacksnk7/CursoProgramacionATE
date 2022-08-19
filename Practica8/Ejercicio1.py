class Auto:
    def __init__(self, marca='Fiat', modelo='Duna', km='0'):
        self.marca = marca
        self.modelo = modelo
        self.km = km

    def kilometraje(self):
        print(self.km)

    def recorrido(self, velocidad='0', distancia=''):
        self.km += distancia

auto1 = Auto('Ford', 'Ka', 5000)
auto1.kilometraje()
auto1.recorrido(100, 15000)
auto1.kilometraje()