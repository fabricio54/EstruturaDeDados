class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            aux = self.head
            while aux.prox:
                aux = aux.prox
            aux.prox = No(elem)
        else:
            self.head = No(elem)
        self._size += 1

    def len(self):
        return self._size

    def __str__(self):
        aux = self.head
        for i in range(self.len()):
            print(aux.dado)
            aux = aux.prox

    def str(self):
        self.__str__()

    def remove(self):
        if self.head:
            aux = self.head
            while aux.prox:
                aux = aux.prox
            del aux

lista = Linkedlist()
lista.append(3)
lista.append(4)
lista.append(2)
lista.append(6)

print('lista atual: ')
lista.str()

print('lista modificada: ')
lista.remove()
lista.str()
