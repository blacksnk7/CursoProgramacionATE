class Tanque_de_butano:
    def __init__(self, capacidad=10):
        self.capacity = capacidad
    def recargar(self, ammount=10):
        self.capacity = ammount
    def esta_vacio(self):
        if (self.capacity > 0):
            return False
        else:
            return True
    def consumir_encendido(self):
        self.capacity -= 1
    def cantidad_de_combustible(self):
        print(f'Resta un {self.capacity * 10}% de la carga.')


class Encendedor:
    last_num = 0

    def __init__(self):
        self.state = 'Apagado'
        self.tank = Tanque_de_butano()
        self.num = Encendedor.last_num + 1
        Encendedor.last_num += 1

    def apagar(self):
        if (self.state == 'Apagado'):
            print('El encendedor ya se encuentra apagado')
        else:
            self.state = 'Apagado'
            print('Encendedor apagado.')

    def encender(self):
        if (self.state == 'Encendido'):
            print('El encendedor ya se encuentra encendido')
        else:
            if (self.tank.esta_vacio()):
                print('No hay suficiente combustible.')
            else:
                self.tank.consumir_encendido()
                self.state = 'Encendido'
                print('Encendedor encendido.')

    def recargar_combustible(self):
        self.tank.recargar()
        print('Tanque llenado.')
    
    def num_serie(self):
        print(f'El numero de serie del encendedor es: {self.num}')

def test():
    '''This tests the functionality of the object "Encendedor".'''
    e1 = Encendedor()
    for i in range(10):
        e1.encender()
        e1.apagar()
    e1.encender()
    e1.recargar_combustible()
    e1.encender()
    e1.num_serie()

test()