class Pila:
    def __init__(self, elements=[]):
        self.elements = elements
    def apilar(self, elemento):
        self.elements.append(elemento)
    def desapilar(self):
        return self.elements.pop(-1)
    def top(self):
        return self.elements[0]
    def vacia(self):
        if (len(self.elements) > 0):
            return False
        else:
            return True
    def cantidad_elementos(self):
        return len(self.elements)

def test():
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

test()