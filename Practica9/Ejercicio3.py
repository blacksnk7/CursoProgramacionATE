import random as r

class Cuenta_bancaria:
    def __init__(self, monto=0, titular="None"):
        self.__saldo = monto
        self.set_titular(titular)
    def get_saldo(self):
        return self.__saldo
    def get_titular(self):
        return self.__titular
    def set_saldo(self, monto):
        self.__saldo += monto
    def set_titular(self, titular):
        self.__titular = titular
        
    def depositar(self, monto):
        self.__saldo += monto
    def extraer(self, monto):
        self.set_saldo_extraido(monto)
        self.set_saldo(-monto)
        return True
    def transferir(self, cuenta, monto):
        monto = monto * 0.991
        if (monto > self.get_saldo()):
            print(f"Usted carece de los fondos para realizar la transferencia de {monto}$. Su balance actual es de: {self.get_saldo}")
        else:
            self.set_saldo(-monto)
            cuenta.set_saldo(monto)
            
class Cuenta_ahorro(Cuenta_bancaria):
    def __init__(self, monto=0, titular="NONE"):
        super().__init__(monto, titular)
        self.set_limite(30000)
        self.saldo_extraido = 0
    def get_limite(self):
        return self.__limite
    def get_saldo_extraido(self):
        return self.__saldo_extraido
    def set_limite(self, limite):
        self.__limite = limite
    def set_saldo_extraido(self, monto):
        self.__saldo_extraido -= monto
        
    def extraer(self, monto):
        if (monto > self.get_saldo()):
            print(f"Usted carece de los fondos para realizar la extraccion requerida de {monto}$, sus fondos actuales son de: {self.saldo_disponible()}$")
            return False
        elif (monto > self.get_saldo_extraido()):
            print(f"Usted no puede retirar la cantidad deseada de {monto}$ ya que su maximo actual de extraccion es de: {self.get_saldo_extraido()}")
            return False
        else:
            super().extraer(monto)
    def modificar_limite_extraccion(self, monto):
        if (monto < self.get_limite()):
            self.set_limite(monto)
            print(f"Se ha cambiado su limite de exraccion a {monto}$ diarios.")
            return True
        else:
            choice = r.randrange(0, 2)
            if (choice == 0):
                print("Su solicitacion para cambiar su limite de extraccion ha sido rechazada.")
                return False
            else:
                self.set_limite(monto)
                print(f"Se ha cambiado su limite de exraccion a {monto}$ diarios.")
                return True
                
class Cuenta_corriente(Cuenta_bancaria):
    def __init__(self, monto=0, titular="NONE"):
        super().__init__(monto, titular)
        self.set_limite(50000)
        self.__saldo_extraido = 0
        self.set_descubierto(10000)
    def get_limite(self):
        return self.__limite
    def get_saldo_extraido(self):
        return self.__saldo_extraido
    def get_descubierto(self):
        return self.__descubierto
    def set_limite(self, limite):
        self.__limite = limite
    def set_saldo_extraido(self, monto):
        self.__saldo_extraido -= monto
    def set_descubierto(self, monto):
        self.__descubierto = monto
        
    def extraer(self, monto):
        if (monto > self.get_saldo()):
            print(f"Usted carece de los fondos para realizar la extraccion requerida de {monto}$, sus fondos actuales son de: {self.saldo_disponible()}$")
            return False
        elif (monto > self.get_saldo_extraido()):
            print(f"Usted no puede retirar la cantidad deseada de {monto}$ ya que su maximo actual de extraccion es de: {self.get_saldo_extraido()}")
            return False
        else:
            super().extraer(monto)
    def modificar_limite_extraccion(self, monto):
        if (monto < self.get_limite()):
            self.set_limite(monto)
            print(f"Se ha cambiado su limite de exraccion a {monto}$ diarios.")
            return True
        else:
            choice = r.randrange(0, 2)
            if (choice == 0):
                print("Su solicitacion para cambiar su limite de extraccion ha sido rechazada.")
                return False
            else:
                self.set_limite(monto)
                print(f"Se ha cambiado su limite de exraccion a {monto}$ diarios.")
                return True
    def modificar_descubierto(self, monto):
        if (monto < self.get_descubierto()):
            self.set_descubierto(monto)
            print(f"Se ha cambiado su monto descubierto a {monto}$.")
            return True
        else:
            choice = r.randrange(0, 2)
            if (choice == 0):
                print("Su solicitacion para cambiar su monto descubierto ha sido rechazada.")
                return False
            else:
                self.set_descubierto(monto)
                print(f"Se ha cambiado su monto descubierto a {monto}$.")
                return True