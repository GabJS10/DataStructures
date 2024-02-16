from nodo import Nodo

class ListaSimpleEnlazada():
    def __init__(self):
        self.primer_nodo = None
        self.ultimo_nodo = None
        

    def vacia(self):
        return self.primer_nodo == None

    def AgregarUltimo(self,dato):
        if self.vacia():
            self.primer_nodo = Nodo(dato)
            self.ultimo_nodo = self.primer_nodo

        else:
            aux = Nodo(dato)
            self.ultimo_nodo.siguiente = aux
            self.ultimo_nodo = aux

    def AgregarPrimero(self,dato):
        if self.vacia():
            self.primer_nodo = Nodo(dato)
            self.ultimo_nodo = self.primer_nodo
        else:
            aux = Nodo(dato)    
            aux.siguiente = self.primer_nodo
            self.primer_nodo = aux

    def eliminar_ultimo(self):
        aux = self.primer_nodo
        while aux.siguiente != self.ultimo_nodo:
            aux = aux.siguiente

        aux.siguiente = None
        self.ultimo_nodo = aux    

    def eliminar_inicio(self):
        aux = self.primer_nodo
        self.primer_nodo = aux.siguiente
        del(aux) 

    def recorrer(self):
        aux = self.primer_nodo
        while aux!=None:
            print(aux.dato)
            aux = aux.siguiente       

                