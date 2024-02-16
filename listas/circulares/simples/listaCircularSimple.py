from nodos import Nodo

class listaCircularSimple():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacia(self):
        return self.primero == None

    def agregar_inicio(self,dato):
        if self.estaVacia():
            self.primero = Nodo(dato)
            self.ultimo = self.primero
            self.ultimo.siguiente = self.primero

        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero



    def agregar_final(self,dato):
        if self.estaVacia():
            self.primero = Nodo(dato)
            self.ultimo = self.primero
            self.ultimo.siguiente = self.primero

        else:
            aux = Nodo(dato)
            self.ultimo.siguiente = aux
            aux.siguiente = self.primero
            self.ultimo = aux

    def eliminar_inicio(self):
        if self.estaVacia():
            print('la lista esta vacia')

        elif self.primero.siguiente == None:
            self.primero = None
            self.ultimo = None
        else:
            aux = self.primero
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero
            del(aux)

    def eliminar_final(self):
        if self.estaVacia():
            print('la lista esta vacia')

        elif self.primero.siguiente == None:
            self.primero = None
            self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente

            aux.siguiente = self.primero
            self.ultimo = aux
                


    def recorrer(self):
        aux = self.primero

        try:
          while aux != self.ultimo:
               print(aux.dato)
               aux = aux.siguiente
          else:
               print(aux.dato)

        except AttributeError:
            print('La lista esta vacia')
                   

