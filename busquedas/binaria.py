lista =[1, 2, 5, 5, 6, 8, 8, 12, 12, 21, 23, 25, 34, 42, 57, 62, 74, 75, 86, 98]

def busqueda_binaria(dato,lista):
    izquierda = 0
    derecha = len(lista)-1

    while izquierda<=derecha:
        medio = (izquierda+derecha)//2

        if dato == lista[medio]:
            return medio
        elif dato<lista[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1
     
    return None           
     

def buscar(dato,lista):
    for i in range(len(lista)):
        print('[{0}] => {1}'.format(i,lista[i]))

    if busqueda_binaria(dato,lista)is not None:
        return 'Se encontro el dato {0} en la posicion {1}'.format(dato,busqueda_binaria(dato,lista))
    else:
        return 'No se encontro el dato'
    

print(buscar(1,lista))