class Registro_vendas:
  def __init__(self,nome,valor):
    self.nome = nome
    self.valor = valor

class Supermercado:
  def __init__(self,nome_supermercado,nome_venda,valor):
    self.nome_supermercado = nome_supermercado
    self.nome_venda = Registro_vendas(nome_venda,valor)
    self.proximo = None

class Sistema:
  def __init__(self):
    self.cabeca = None
    self.Valor_final = 0

  def cadastro(self,nome_supermecado,nome_venda,valor):
    if self.cabeca:
      aux = self.cabeca
      while aux.proximo:
        aux = aux.proximo
      aux.proximo = Supermercado(nome_supermecado,nome_venda,valor)
      self.Valor_final += valor
    else:
      self.cabeca = Supermercado(nome_supermecado,nome_venda,valor)
      self.Valor_final += valor

  def Remover(self,nome_supermercado,valor):
    if self.cabeca:
      aux = self.cabeca
      while aux.proximo and aux.nome_supermercado != nome_supermercado:
        aux = aux.proximo
      if aux.nome_supermercado == nome_supermercado:
        aux.nome_venda.valor -= valor
        aux.venda_nome = ''

      else:
        print('Error :(')
    else:
      print('A lista encontra-se vazia :(:(')
  def Imprimir(self):
    if self.cabeca:
      aux = self.cabeca
      while aux:
        print(f'Nome do supermercado:{aux.nome_supermercado}')
        print(f'Nome da venda:{aux.nome_venda.nome}')
        print(f'valor:{aux.nome_venda.valor}')
        aux = aux.proximo


Nome_supermercado = Sistema()
Nome_supermercado.cadastro('Redenção','óleo',1400)
Nome_supermercado.cadastro('Soares','carne bovina',3600)
Nome_supermercado.cadastro('Sertanejo','leite em pó camponesa',800)
Nome_supermercado.cadastro('Bom preço','Margarina primor',3750)

Nome_supermercado.Imprimir()
print()
print()
print()
print()
Nome_supermercado.Remover('Sertanejo',800)
print('Sistema de compra atualizada com a remoção do nome da compra e valor:')
Nome_supermercado.Imprimir()
