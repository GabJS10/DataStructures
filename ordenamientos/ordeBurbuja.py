lista = [2,6,4,9,7,1]

#ciclo for que se encarga de recorrer toda la lista
for i in range(len(lista)):
     print('Pasada numero {0}'.format(i))
     #ciclo for que se encarga de ordenar la lista por cada vez que se recorra
     for x in range(len(lista)-1):
        if lista[x] > lista[x+1]:
            numaux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = numaux
            print(lista)

          
          