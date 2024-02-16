lista = [2,6,4,9,7,1]
#for que recorre toda la lista
for i in range(len(lista)):
    #se va capturando el indice actual
    minimo = i
    #se empieza a recorres desde el indice actual o i+1 para que no se comprar con el mismo
    #for que guarda el indice del numero menor en cada recorrido
    for x in range(i+1,len(lista)):
        #print(x)
        #si el valor del indice actual es menor, se guarda su indice en la variable minimo
        if lista[x] < lista[minimo]:
            minimo = x
    #Se hace el reemplazo de valores            
    aux = lista[i]
    lista[i] = lista[minimo]
    lista[minimo] = aux
    print(lista)
print(lista)    