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

class ControlRemoto:
    def __init__(self, television=TV()):
        self.tv = television
        self.old_channel = television.canal_actual()
    def asignar(self, un_TV):
        self.tv = un_TV
    def encender(self):
        self.tv.encender()
    def apagar(self):
        self.tv.apagar()
    def canal_up(self):
        self.old_channel = self.tv.canal_actual()
        self.tv.canal_up()
    def canal_down(self):
        self.old_channel = self.tv.canal_actual()
        self.tv.canal_down()
    def cambiar_a_canal(self, canal):
        self.old_channel = self.tv.canal_actual()
        self.tv.cambiar_a_canal(canal)
    def canal_previo(self):
        current_channel = self.tv.canal_actual()
        self.tv.cambiar_a_canal(self.old_channel)
        self.old_channel = current_channel
    def volume_up(self):
        self.tv.volume_up()
    def volume_down(self):
        self.tv.volume_down()
    def mute(self):
        self.tv.cambiar_a_volumen(0)
    def info_canal(self):
        print(f"Usted esta viendo el canal: {self.tv.canal_actual()}")
    