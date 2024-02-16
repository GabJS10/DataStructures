from nodos import Nodo

class BinarySearchTree():
    def __init__(self):
        self.root= None


    def is_empty(self):
        return self.root == None
    
    def add(self,value):
        if self.is_empty():
            self.root = Nodo(value=value)
        else:
            node = self.__get_place(value=value)

            if value<= node.value:
                node.left = Nodo(value=value, parent=node,is_left=True)
            else:
                node.right = Nodo(value=value, parent=node,is_right=True)
                    
    
    def __get_place(self,value):
        aux = self.root
        while aux:
            temp = aux
            if value<=aux.value:
                aux = aux.left
            else:
                aux = aux.right
        return temp           
    
    #izquierda-raiz-derecha
    def show_in_orden(self,node):
        if node:
            self.show_in_orden(node.left)
            print(node.value)
            self.show_in_orden(node.right)
    #raiz-izquierda-derecha
    def show_pre_orden(self,node):
        if node:
            print(node.value)
            self.show_pre_orden(node.left)
            self.show_pre_orden(node.right)

    #izquierda-derecha-raiz
    def show_post_orden(self,node):
        if node:
            self.show_post_orden(node.left)
            self.show_post_orden(node.right)
            print(node.value)
            

    def search(self,node,value):
        if node == None:
            return None
        else:
            if node.value == value:
                return node
            elif value<=node.value:
                return self.search(node=node.left,value=value)
            else:
                return self.search(node=node.right,value=value)


