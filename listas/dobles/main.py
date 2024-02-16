from listaDobleEnlazada import listaDobleEnlazada


lista = listaDobleEnlazada()

lista.agregar_final(12)
lista.agregar_final(5)
lista.agregar_final(58)
lista.agregar_final(19)
lista.agregar_final(99)

lista.recorrer_desde_inicio()
print('********************')
lista.recorrer_desde_final()
