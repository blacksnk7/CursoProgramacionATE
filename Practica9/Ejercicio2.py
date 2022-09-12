class Estructura_de_datos:
    def __init__(self, elements=[]):
        self.__elements = elements
    def vacia(self):
        if (len(self.elements) > 0):
            return False
        else:
            return True
    def cantidad_elementos(self):
        return len(self.elements)

class Pila(Estructura_de_datos):
    def apilar(self, elemento):
        self.__elements.append(elemento)
    def desapilar(self):
        return self.__elements.pop(-1)
    def top(self):
        return self.__elements[-1]
    
class Cola(Estructura_de_datos):
    def encolar(self, elemento):
        self.__elements.append(elemento)
    def desencolar(self):
        return self.__elements.pop(0)
    def top(self):
        return self.__elements[0]
    
def test_pila():
    '''Tests the functionality of the object "Pila"'''
    p = Pila()
    print(p.vacia())
    print(p.cantidad_elementos())
    p.apilar(1)
    p.apilar(2)
    p.apilar(3)
    print(p.vacia())
    print(p.cantidad_elementos())
    print(p.top())
    print(p.desapilar())
    print(p.top())
    print(p.desapilar())
    print(p.top())
    print(p.desapilar())
    print(p.vacia())
    print(p.cantidad_elementos())
    
def test_cola():
    '''Tests the functionality of the object "Pila"'''
    p = Cola()
    print(p.vacia())
    print(p.cantidad_elementos())
    p.encolar(1)
    p.encolar(2)
    p.encolar(3)
    print(p.vacia())
    print(p.cantidad_elementos())
    print(p.top())
    print(p.desencolar())
    print(p.top())
    print(p.desencolar())
    print(p.top())
    print(p.desencolar())
    print(p.vacia())
    print(p.cantidad_elementos())

print("-PILA-")
test_pila()
print("-COLA-")
test_cola()