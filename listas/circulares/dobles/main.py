from listaDobleCircular import ListaDobleCircular



lista = ListaDobleCircular()

lista.insertar_al_final(13)
lista.insertar_al_final(4)
lista.insertar_al_final(78)
lista.insertar_al_final(33)
lista.insertar_al_final(21)


lista.eliminar_final()
lista.eliminar_inicio()
lista.recorrer_desde_inicio()
print('*' * 10)
lista.recorrer_desde_final()
print('*' * 10)
print(lista.primero.anterior.dato)
print(lista.ultimo.siguiente.dato)
print(f'Dato encontrado: {lista.buscar(4)}')