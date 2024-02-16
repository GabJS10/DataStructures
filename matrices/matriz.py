'''filas = 5
columnas = 5

matriz = []
for f in range(filas):
    matriz.append([])
    for c in range(columnas):
        matriz[f].append(None)


for m in matriz:
    print(m)'''


#con comprension de listas

matriz = [list(range(5)) for x in range(5)]

for m in matriz:
    print(m)
