class Vehiculo:
    def __init__(self, kms=0, tank=-1, consumption=-1, fuel_cost=-1, autonomia=-1):
        self.set_kms(kms)
        self.set_tank(tank)
        self.set_max_tank(tank)
        self.set_consumption(consumption)
        self.set_fuel_cost(fuel_cost)
        self.set_autonomia(autonomia)
    def get_kms(self):
        return self.__kms
    def get_tank(self):
        return self.__tank
    def get_max_tank(self):
        return self.__max_tank
    def get_consumption(self):
        return self.__consumption
    def get_fuel_cost(self):
        return self.__fuel_cost
    def get_autonomia(self):
        return self.__autonomia
    def set_kms(self, kms):
        self.__kms = kms
    def set_tank(self, tank):
        self.__tank = tank
    def set_max_tank(self, tank):
        self.__max_tank = tank
    def set_consumption(self, consumption):
        self.__consumption = consumption
    def set_fuel_cost(self, fuel_cost):
        self.__fuel_cost = fuel_cost
    def set_autonomia(self, autonomia):
        self.__autonomia = autonomia
        
        
    def recorrido(self, distance):
        if (distance <= self.get_autonomia()):
            fuel = self.get_tank() - (distance / self.get_consumption())
            self.set_tank(fuel())
            self.set_autonomia(self.get_autonomia() - distance)
        else:
            fuel_needed = (distance - self.get_autonomia()) / self.get_consumption()
            cost = fuel_needed * self.get_fuel_cost()
            print(f"No es posible realizar el viaje. Se requieren de {fuel_needed:.2f} litros de nafta extra, lo que costara {cost:.2f}$")
    def cargar_combustible(self, fuel):
        possible_fuel = self.get_max_tank() - self.get_tank()
        if (fuel > possible_fuel):
            fuel = possible_fuel
        price = fuel * self.get_fuel_cost()
        print(f"El precio para cargar {fuel:.2f} litros de combustible es de: {price:.2f}")
    def llenar_tanque(self):
        possible_fuel = self.get_max_tank() - self.get_tank()
        price = possible_fuel * self.get_fuel_cost()
        print(f"El precio para cargar {possible_fuel:.2f} litros de combustible es de: {price:.2f}")
            
        
class Auto(Vehiculo):
    __max_tank = 51.0
    
    def __init__(self):
        super().__init__(0, 51.0, 16.3, 172.3, 831.3)
        print(self.__max_tank)
        
class Moto(Vehiculo):
    __max_tank = 14.3
    
    def __init__(self):
        super().__init__(0, 14.3, 30.8, 139.0, 440.44)
        
class Camioneta(Vehiculo):
    __max_tank = 80.0
    
    def __init__(self):
        super().__init__(0, 80.0, 10.53, 197.0, 842.4)
        
class Camion(Vehiculo):
    __max_tank = 294.0
    
    def __init__(self):
        super().__init__(0, 294.0, 3.34, 144.8, 981.86)
        
def test():
    a = Auto()
    a.llenar_tanque()
    a.get_tank()
    a.recorrido(1200)
    a.llenar_tanque()
    
test()
    