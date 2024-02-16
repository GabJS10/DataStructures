class Pila():
    
    def __init__(self,size):
        self.lista = []
        self.tope = 0
        self.size = size


    def empty(self):
        if self.tope==0:
            return True
        else:
            return False
    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope+=1
        else:
            #print('La pila esta llena')
            #codigo para volver lapila dinamica
            self.size+=1
            self.lista += [dato]
            self.tope+=1
            print('se ha incrementado el tamaño de la pila')

    def pop(self):
        if self.empty():
            print('la lista esta vacia')
        else:
            #tam 5 (0,1,2,3,4)
            self.tope-=1
            #tam 4(0,1,2,3) 
            #metodo range, tamaño 4, resta uno para evitar errores en indice queda (0,1,2,3)
            #recorremos sin el ultimo indice, eliminando ese elemento
            self.lista = [self.lista[x] for x in range(self.tope)] 

    def show(self):
        '''for x in range(self.tope):
            print('[{0}] => {1}'.format(x,self.lista[x]))'''
        cont = self.tope-1
        while cont>=0:
          print('[{0}] => {1}'.format(cont,self.lista[cont]))
          cont-=1
     

 
    def Size(self):
        return self.tope

    def peek(self):
        return self.lista[-1]            
                    
            
               
            
