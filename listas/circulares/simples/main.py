from listaCircularSimple import listaCircularSimple



lista = listaCircularSimple()

lista.agregar_final(12)
lista.agregar_final(3)
lista.agregar_final(45)
lista.agregar_final(37)
lista.agregar_final(88)

lista.agregar_inicio(10)

lista.eliminar_final()
lista.eliminar_inicio()
lista.recorrer()

print(lista.primero)
print(lista.ultimo.siguiente)