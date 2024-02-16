lista = [6,98,23,1,5,8,42,57,21,2,5,8,34,12,62,12,74,25,86,75]



for i in range(1,len(lista)):
    aux = lista[i]
    izquierda = i - 1

    while izquierda>=0 and aux<lista[izquierda]:
        lista[izquierda+1] = lista[izquierda]
        lista[izquierda] = aux
        izquierda-=1     
        print(lista)

print(lista)        