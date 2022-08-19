class TV:
    first_channel = 2
    last_channel = 135

    def __init__(self):
        self.state = "Apagado"
        self.current_channel = TV.first_channel
        self.volume = 10
    def encender(self):
        self.state = "Encendido"
        print(f"TV encendida en el canal {self.canal_actual()}.")
    def apagar(self):
        self.state = "Apagado"
        print("TV apagada.")
    def canal_up(self):
        if (self.current_channel < TV.last_channel):
            self.current_channel += 1
        else:
            self.current_channel = TV.first_channel
    def canal_down(self):
        if (self.current_channel > TV.first_channel):
            self.current_channel -= 1
        else:
            self.current_channel = TV.last_channel
    def cambiar_a_canal(self, canal):
        if (canal > TV.last_channel) or (canal < TV.first_channel):
            print("Ese canal no existe.")
        else:
            self.current_channel = canal
    def canal_actual(self):
        return self.current_channel
    def volume_up(self):
        if (self.volume < 10):
            self.volume += 1
    def volume_down(self):
        if (self.volume > 0):
            self.volume -= 1
    def volume_actual(self):
        return self.volume
    def cambiar_a_volumen(self, volumen):
        if (volumen > 10) or (volumen < 0):
            print("Volumen incorrecto. El volumen debe encontrarse entre 0 y 10")
        else:
            self.volume = volumen

def test():
    '''This tests the functionality of the object "TV".'''
    television = TV()
    television.encender()
    television.cambiar_a_canal(4)
    print(f"Canal: {television.canal_actual()}")
    television.canal_up()
    print(f"Canal: {television.canal_actual()}")
    television.canal_up()
    print(f"Canal: {television.canal_actual()}")
    print(f"Volumen: {television.volume_actual()}")
    television.cambiar_a_volumen(0)
    print(f"Volumen: {television.volume_actual()}")
    television.volume_up()
    print(f"Volumen: {television.volume_actual()}")
    television.apagar()
    
test()