from arbol import BinarySearchTree

arbol = BinarySearchTree()

arbol.add(8)
arbol.add(10)
arbol.add(3)
arbol.add(14)
arbol.add(13)
arbol.add(1)
arbol.add(6)
arbol.add(4)
arbol.add(7)

'''arbol.show_in_orden(arbol.root)
print('*' * 10)
arbol.show_pre_orden(arbol.root)
print('*' * 10)
arbol.show_post_orden(arbol.root)'''

print(arbol.search(arbol.root,7).parent.value)