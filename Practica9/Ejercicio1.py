class Animal:
    def hablar(self, msj):
        print(msj)
    def quien_sos(self, msj):
        print(f"Soy un {msj}")
    
class Gato(Animal):
    def hablar(self):
        super().hablar("Miau!")
    def quien_sos(self):
        race = type(self).__name__
        super().quien_sos(race)
        
class Perro(Animal):
    def hablar(self):
        super().hablar("Guau!")
    def quien_sos(self):
        race = type(self).__name__
        super().quien_sos(race)
        
class Pollo(Animal):
    def hablar(self):
        super().hablar("Pio!")
    def quien_sos(self):
        race = type(self).__name__
        super().quien_sos(race)
        
class Humano(Animal):
    def hablar(self):
        super().hablar("¡Hola!")
    def quien_sos(self):
        race = type(self).__name__
        super().quien_sos(race)
    
    
test = Gato()
test.quien_sos()