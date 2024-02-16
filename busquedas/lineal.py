lista = [6,98,23,1,5,8,42,57,21,2,5,8,34,12,62,12,74,25,86,75]


def busqueda_lineal(dato,lista):
     for i in range(len(lista)):
          if lista[i] == dato:
               return i
     return None     
def buscar(dato,lista):
     for i in range(len(lista)):
          print("[{0} => {1}]".format(i,lista[i]))
     if busqueda_lineal(dato,lista):
          return "El dato {0} se encontro en el indice {1}".format(dato,busqueda_lineal(dato,lista))
     else:
          return "No se encontro el dato"
     
print(buscar(100,lista))     