from Nodos import Nodo


class ListaDobleCircular():
    def __init__(self):
        self.primero = None
        self.ultimo = None


    def vacia(self):
        return self.primero == None

    def insertar_al_inicio(self,dato):
        if self.vacia():
            self.primero = Nodo(dato)
            self.ultimo = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero    

    def insertar_al_final(self,dato):
        if self.vacia():
            self.primero = Nodo(dato)
            self.ultimo = self.primero
        else:
            aux = Nodo(dato)
            self.ultimo.siguiente = aux
            aux.anterior = self.ultimo
            self.ultimo = aux
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo

    def eliminar_inicio(self):
        if self.vacia():
            print('lista vacia')
        elif self.primero.siguiente == None:
            self.primero = None
            self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero

    
    def eliminar_final(self):
        if self.vacia():
            print('lista vacia')
        elif self.primero.siguiente == None:
            self.primero = None
            self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo

    def buscar(self,dato):  
        aux = self.primero
        while aux != self.ultimo:
            if aux.dato == dato:
                return True
            aux = aux.siguiente
        else:
            if aux.dato == dato:
                return True

        return False    

    def recorrer_desde_inicio(self):
        aux = self.primero
        while aux != self.ultimo:
            print(aux.dato)
            aux = aux.siguiente
        else:
            print(aux.dato)    

    def recorrer_desde_final(self):
        aux = self.ultimo
        while aux != self.primero:
            print(aux.dato)
            aux = aux.anterior
        else:
            print(aux.dato)    
            

