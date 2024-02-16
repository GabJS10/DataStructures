from ListaSimpleEnlazada import ListaSimpleEnlazada

lista = ListaSimpleEnlazada()

lista.AgregarUltimo(77)
lista.AgregarUltimo(33)
lista.AgregarUltimo(5)
lista.AgregarUltimo(21)
lista.AgregarUltimo(30)

lista.AgregarPrimero(20)
lista.recorrer()

lista.eliminar_ultimo()
print('*****************')
lista.recorrer()

print('*****************')
lista.eliminar_inicio()
lista.recorrer()

print('*****************')
lista.eliminar_inicio()
lista.recorrer()