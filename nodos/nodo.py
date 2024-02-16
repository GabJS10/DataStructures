class Nodo():
    def __init__(self,dato,siguiente = None):
        self.dato = dato
        self.siguiente = siguiente


def recorrer(nodo):
    while nodo != None:
        print(nodo.dato)
        nodo = nodo.siguiente
        
nodo5 = Nodo(23)        
nodo4 = Nodo(45,nodo5)        
nodo3 = Nodo(11,nodo4)        
nodo2 = Nodo(72,nodo3)        
nodo1 = Nodo(21,nodo2)        
        
recorrer(nodo=nodo1)                