from random import randint

def matriculas(mat, lista):
    if mat is None:
        lista.append(mat)
        return False
    elif mat in lista:
        return True
    return False

class Aluno:
    def __init__(self, nome, matricula, disciplinas=None):
        self.nome = nome
        self.disciplinas = disciplinas
        self.notas = []
        self.matricula = matricula

class Sistema:
    def __init__(self, aluno=None):
        self.aluno = aluno
        self.left = None
        self.right = None

    def insert(self, aluno, matricula):
        if not self.aluno:
            self.aluno = aluno
        elif matricula > self.aluno.matricula:
            if self.left:
                self.left.insert(aluno, matricula)
            else:
                self.left = Sistema(aluno)
        elif matricula < self.aluno.matricula:
            if self.right:
                self.right.insert(aluno, matricula)
            else:
                self.right = Sistema(aluno)

    def altura(self):
        if not self.aluno:
            return -1
        else:
            alt_e = self.left.altura() if self.left else -1
            alt_d = self.right.altura() if self.right else -1
            return alt_e + 1 if alt_e > alt_d else alt_d + 1

    def gerar_lista(self, lista):
        if self.aluno:
            if self.left:
                self.left.gerar_lista(lista)
            lista.append(self.aluno)
            if self.right:
                self.right.gerar_lista(lista)
        return lista


    def destruir(self):
        if self.aluno:
            if self.left:
                self.left.destruir()
            if self.right:
                self.right.destruir()
            del self.aluno
            del self


    def gerar_arvore(self, lista, ini, fim):
        meio = (ini + fim) // 2
        self.aluno = lista[meio]
        if ini <= meio - 1:
            self.left = Sistema()
            self.left.gerar_arvore(lista, ini, meio - 1)
        else:
            self.left = None
        if meio + 1 <= fim:
            self.right = Sistema()
            self.right.gerar_arvore(lista, meio + 1, fim)
        else:
            self.right = None
        return self


    def procurar(self, matricula):
        if not self.aluno:
            return False
        elif self.aluno.matricula is matricula:
            return True
        elif self.left and matricula < self.aluno.matricula:
            self.left.procurar(matricula)
        elif self.right and matricula > self.aluno.matricula:
            self.right.procurar(matricula)



    def insert_disciplinas(self, matricula, disciplinas):
        if self.aluno.matricula is matricula:
            self.aluno.disciplinas = disciplinas
            for i in range(len(self.aluno.disciplinas)):
                self.aluno.notas.append([])
        elif matricula > self.aluno.matricula and self.left:
            self.left.insert_disciplinas(matricula, disciplinas)
        elif matricula < self.aluno.matricula and self.right:
            self.right.insert_disciplinas(matricula, disciplinas)


    def insert_notas(self, matricula, disciplina, nota):
        if self.aluno.matricula is matricula:
            for i in range(len(self.aluno.disciplinas)):
                if self.aluno.disciplinas[i] == disciplina:
                    self.aluno.notas[i] = nota
        elif matricula > self.aluno.matricula and self.left:
            self.left.insert_disciplinas(matricula, disciplinas)
        elif matricula < self.aluno.matricula and self.right:
            self.right.insert_disciplinas(matricula, disciplinas)


    def imprimir_disciplinas(self, matricula):
        if self.aluno.disciplinas is matricula:
            print('Disciplinas: ',self.aluno.disciplina)
        elif matricula > self.aluno.matricula and self.left:
            self.left.imprimir_disciplinas(matricula)
        elif matricula < self.aluno.matricula and self.right:
            self.right.imprimir_disciplinas(matricula)

    def remove_disciplina(self, matricula, disciplina):
        if self.aluno.disciplinas is matricula:
            for i in range(len(self.aluno.disciplinas)):
                if self.aluno.disciplinas[i] is disciplina:
                    self.aluno.notas[i] = [0, 0]
            self.aluno.disciplinas.remove(disciplina)
        elif matricula > self.aluno.matricula and self.left:
            self.left.remove_disciplina(matricula, disciplina)
        elif matricula < self.aluno.matricula and self.right:
            self.right.remove_disciplina(matricula, disciplina)


    def imprimir(self):
        if not self.aluno:
            print()
        else:
            if self.right:
                self.right.imprimir()
            print('Nome: ',self.aluno.nome)
            print('Disciplinas: ', self.aluno.disciplinas)
            print('Notas: ', self.aluno.notas)
            print('Matricula: ', self.aluno.matricula)
            print()
            if self.left:
                self.left.imprimir()


def Menu(arvore):
    nome = ''
    lista_mat = []

    op = 's'
    while op in 'sS':
        print(" <<<< SISTEMA DE CADASTRAMENTO DE ALUNOS E DISCIPLINAS >>>>")
        print("""[ 1 ] Cadastrar Aluno
[ 2 ] Cadastrar Disciplina
[ 3 ] Cadastrar Nota em Disciplina
[ 4 ] Remover Aluno
[ 5 ] Remover Disciplina de Aluno
    """)
        opcao = int(input('Informe uma Opção: '))
        if opcao == 1:
            nome = str(input('Informe o nome: '))
            matricula = randint(1, 100)
            while matriculas(matricula, lista_mat):
                matricula = randint(1, 100)
            arvore.insert(Aluno(nome, matricula), matricula)
            print('<<< CADASTRO REALIZADO >>>')
            print(f'NOME: {nome}\nMATRICULA: {matricula}')

        if opcao == 2:
            mat = int(input('Informe o Número da Matricula: '))
            if arvore.procurar(mat):
                q = int(input('Informe a quantidades de Disciplinas: '))
                disciplinas = []
                for i in range(q):
                    disciplinas.append(input(f'Informe a disciplina {i+1}: '))
                arvore.insert_disciplinas(mat, disciplinas)
            else:
                print('Número de Matricula não encontrada!!!"')

        if opcao == 3:
            mat = int(input('Informe o número da Matricula: '))
            if arvore.procurar(mat):
                arvore.imprimir_disciplinas(mat)
                disc = str(input('Informe a Disciplina para Adicionar as Notas: '))
                notas = []
                for i in range(2):
                    notas.append(int(input(f'Informe a {i+1} nota da disciplina de {disc}: ')))
                arvore.insert_notas(mat, disc, notas)
            else:
                print('Número de Matricula não encontrada!!!')

        if opcao == 4:
            lista = []
            lista = arvore.gerar_lista(lista)
            arvore.imprimir()
            aluno = str(input('Informe o Nome do aluno a ser removido: '))
            for i in range(len(lista)-1):
                if lista[i].nome == aluno:
                    lista.remove(lista[i])
            arvore.destruir()
            arvore = arvore.gerar_arvore(lista, 0, len(lista)-1)
            arvore.imprimir()

        if opcao == 5:
            arvore.imprimir()
            mat = int(input('Informe a matricula: '))
            if arvore.procurar(mat):
                arvore.imprimir_disciplinas(mat)
                dis = str(input('Informe a disciplina a ser removida: '))
                arvore.remove_disciplina(mat, dis)

        op = input('Deseja Continuar?')
    arvore.imprimir()

arvore = Sistema()
Menu(arvore)
