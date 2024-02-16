from nodos import Nodo

class listaDobleEnlazada():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0


    def vacia(self):
        return self.primero == None
    
    def agregar_final(self,dato):
        if self.vacia():
            self.primero = Nodo(dato)
            self.ultimo = self.primero
        else:
            aux = Nodo(dato)
            self.ultimo.siguiente = aux
            anterior = self.ultimo
            self.ultimo = aux    
            self.ultimo.anterior = anterior

        self.size+=1


    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = Nodo(dato)
            self.ultimo = self.primero
        else:
            aux = Nodo(dato)    
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux


    def recorrer_desde_inicio(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def recorrer_desde_final(self):
        aux = self.ultimo       

        while aux != None:
            print(aux.dato)
            aux = aux.anterior 

    def eliminar_final(self):
        if self.vacia():
            print('esta vacia')

        elif self.primero.siguiente == None:
            self.primero = None
            self.ultimo = None
            self.size = 0

        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size-=1                                

    def eliminar_inicio(self):
        if self.vacia():
            print('Esta vacia')

        elif self.primero.siguiente == None:
            self.primero = None
            self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size-=1

    def Size(self):
        return self.size                        