class Lista:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.prox = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def inserir(self, nome, salario):
        if self.head:
            aux = self.head
            while aux.prox:
                aux = aux.prox
            aux.prox = Lista(nome, salario)
        else:
            self.head = Lista(nome, salario)

    def procurar(self, nome):
        if self.head:
            aux = self.head
            while aux.prox and aux.nome != nome:
                aux = aux.prox
            if aux.nome == nome:
                return aux.salario
            else:
                return 0


class HashTabela:

    def __init__(self):
        self.tam_max = 10
        self.tabela = [Linkedlist()] * self.tam_max

    def hash(self, chave, nome, salario):
        ini = chave % self.tam_max
        self.tabela[ini].inserir(nome, salario)

    def procurar(self, chave, nome):
        ini = chave % self.tam_max
        return self.tabela[ini].procurar(nome)


l = HashTabela()

Menu = 1
while Menu != 0:
    Menu = int(input('[1]. INSERIR FUNCIONÁRIO\n[2]. BUSCAR SALÁRIO DO FUNCIONÁRIO\n[0]. SAIR\n'))
    if Menu == 1:
        nome = str(input('Informe o seu nome:')).capitalize()
        salario = float(input('Digite o valor do salário:'))
        chave = ord(nome[0])
        l.hash(chave, nome, salario)
    elif Menu == 2:
        nome = str(input('Informe o nome do funcionário que deseja encontrar:')).capitalize()
        chave = ord(nome[0])
        if l.procurar(chave, nome) != 0:
            print(f'O salário do funcionario {nome} é R$: {l.procurar(chave, nome)}')
        else:
            print(
                'O funcionário não existe! (^_^) Tente fazer a inserção desse funcionário e realize uma nova busca através do menu principal!')

    elif Menu == 0:
        print('SAINDO! Bye Bye (_)')

    else:
        print('Opção inválida!! :-\ Tente novamente fazendo uma nova busca através do menu principal!')
