class Node:
   def __init__(self, cpf, conta):
       self.cpf = cpf
       self.conta = conta
       self.next = None

class Queue:
   def __init__(self):
       self.first = None
       self.last = None
       self._size = 0

   def push(self, cpf, conta):
       node = Node(cpf, conta)
       if self.last is None:
           self.last = node

       else:
           self.last.next = node
           self.last = node

       if self.first is None:
           self.first = node

       self._size = self._size + 1


   def pop(self):
       if self.first is not None:
           # elem = self.first.data
           self.first = self.first.next
           self._size = self._size - 1
          #  return elem
       else:
           raise IndexError("The queue is empty")

   def peek(self):
       if self._size > 0:
           elem = self.first
           return elem
       raise IndexError("the queue is empty")

   def __len__(self):
       return self._size

   def len(self):
       return self.__len__()

   def __repr__(self):
       if self._size > 0:
           pointer = self.first
           while(pointer):
               print("Dados da Conta")
               print(f'Cpf:{pointer.cpf}   Numero da Conta:{pointer.conta}\n\n')
               pointer = pointer.next
       else:
           raise IndexError("the queue is empty")

   def __str__(self):
       self.__repr__()

   def string(self):
       print(self.__str__())



fila = Queue()
op = 's'

while op in 'Ss':
   cpf = str(input('informe o cpf: '))
   conta = int(input('informe o número da conta: '))
   fila.push(cpf, conta)
   op = str(input('insirir nova pessoa na fila: [S/N]'))

opcao = str(input('deseja imprimir os dados das pessoas da fila?\n'))
if opcao in 'Ss':
   print(fila.__str__())

op = 's'
while op in 'Ss':
   op = str(input('deseja remover os dados da primeira pessoa da fila atualmente: [S/N]'))
   if op in 'Ss' and len(fila) > 0:
       fila.pop()
   elif not len(fila) > 0:
       op = 'n'
       print('Não tem elementos na fila de dados!!')
   else:
       print('Saindo do progama...\n')

opcao = str(input('deseja imprimir a fila dos dados das pessoas depois da remoção: [S/N]\n'))

if opcao in 'Ss' and len(fila) > 0:
   fila.string()

elif not len(fila) > 0:
   print('Não tem elementos na fila de dados!!')

else:
   print('Progama Encerrado!!!')
