#SISTEMA DE LANCHONETE
class Pedido(object):
  __taxa = 0.1
  soma = 0

  def __init__ (self, nome, ItensConsumidos):
    self.nome = nome
    self.ItensConsumidos = ItensConsumidos 

  def Valor_Total(self,preco_pedido):
    preco_pedido_total = self.ItensConsumidos*preco_pedido 
    return preco_pedido_total
    
  def Calcular_Total(self,Preco_Total):
    Pedido.soma = Pedido.soma + Preco_Total
    return Pedido.soma
 
    
class Coxinha(Pedido):
  preco = {'Coxinha': 4.5}
  peso = 60
  quantidade_Coxinha = 10
  #Quando for usar um metodo de outra classe se elativer usando um atributo devesse declarar o __init__ dessa outra classe para que o atributo seja visto por toda classe

  #Antes estava dando erro de ItensConsumidos não ser atributo de Coxinha1
  def __init__ (self, nome, ItensConsumidos):
    super().__init__(nome, ItensConsumidos)
    
  def Valor_Total_Coxinha(self, preco_pedido):
    return super().Valor_Total(preco_pedido)
  
  def Diminui_Quantidade_Coxinha(self):
    Coxinha.quantidade_Coxinha -= self.ItensConsumidos
    return Coxinha.quantidade_Coxinha 

class Pastel:
  pass

class Sanduiche:
  pass

#trabalhar com arquivos!
class GerandoNota(object):
  def __init__(self, arquivoNota):
    self.arquivoNota = arquivoNota
    
  def EscrevendoNota(self,Linha):
    #Abre e fecha o arquivo sem precisar close 
    #Estrutura usada para para fazer algo, caso não passo uma mensagem amigavel e que possa entrender
    try:
      with open(self.arquivoNota, 'a') as escreve:
        escreve.write(Linha)
        escreve.write("\n")
    except:
      print("ERRO!!!!")
      
  def ImprimindoNota(self):
    with open(self.arquivoNota, 'r') as escreve:
      #Retorna todas as linhas do arquivo
      escreve.readlines()

  def LimparArquivo(self):
    #Quando abrimos um arquivo no modo de gravação, então para isso não passamos nenhum argumento. Para que assim seja feita a limpeza.
    with open(self.arquivoNota, 'w') as escreve:
      pass

class EnviarNota:
  pass

class Interface:
  pass
#como vamos estrair as chaves desse dicionario, vai ser gerado uma lista do tipo dict_keys, então preciso transformar em lista pura para acessar esse item como é o caso abaixo
# x =list(Coxinha.preco.keys())[0]
# print(x)

#MAIN

def main():
  Nome = input("Informe seu nome: ")
  #LinhaNota = ""
  NotaFiscal = "Nota.txt"
  LinhaNota = "Pedido     Valor     Qtd     Total"
  Escrevendo_na_Nota = GerandoNota(NotaFiscal)
  Escrevendo_na_Nota.LimparArquivo()
  Escrevendo_na_Nota.EscrevendoNota(LinhaNota)
  
  while True:
    Escolha = int(input("Qual o pedido: "))
    Qtd = int(input("Informe a quantidade: "))
    pedir = Pedido(Nome, Qtd)
    cox = Coxinha(Nome,Qtd)
  
    if Escolha == 1:
      preco_Unit = Coxinha.preco['Coxinha']
      Produto_Escolhido = cox.Valor_Total_Coxinha(preco_Unit)
      cox.Diminui_Quantidade_Coxinha()
  
      LinhaNota = list(Coxinha.preco.keys())[0] + "     " + str(preco_Unit) + "       " + str(Qtd) +"       "+ str(Produto_Escolhido)
      
      Escrevendo_na_Nota.EscrevendoNota(LinhaNota)
    else:
      Pedido.soma = 0
      False
  
    print(pedir.Calcular_Total(Produto_Escolhido))
    print(Coxinha.quantidade_Coxinha)

main()
