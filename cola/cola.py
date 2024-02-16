class Cola():
    def __init__(self):
        self.cola = []
        self.size = 0
    def empty(self):
        return len(self.cola) == 0
             

    def push(self,dato):
        self.cola += [dato]
        self.size+=1

    def pop(self):
        if self.empty():
            print('La pila esta vacia')
        else:
            self.cola = [self.cola[x] for x in range(1,self.size)]
            self.size-=1
    def show(self):
        cont = self.size-1

        while cont > -1:
            print('[{0}] => [{1}]'.format(cont,self.cola[cont]))
            cont-=1

    def front(self):
        if self.empty():
            print('Esta vacia')

        else:
            return self.cola[0]                                     
