# Programa de controle de preços desenvolvido pelo
# Codificado pelo aluno de Engenharia de Software Lucas José Pereira - RU: 4057875
 
# Crie um programa que calcule o valor total
# em consideração ao custo da embalagem.
 
# Definir mensagem de bem-vindo ao programa.
def welcome():
   """Uma saudação ao usuário antes de iniciarmos a coleta de dados."""
   print("Bem vindo a calculadora de frete do Lucas J. Pereira")
welcome()


def calcular_frete(valor_produto, quantidade_produto):
   if 0 <= quantidade_produto < 11:
      frete = 30
   elif 11 <= quantidade_produto < 101:
      frete = 60
   elif 101 <= quantidade_produto < 1001:
      frete = 120
   else:
      frete = 240

   return frete


def calcular_valor_total(subtotal, frete):
   valor_total = subtotal + frete
   print("Este será o valor total sem o frete: R$ {:.2f}".format(subtotal))
   print("Este será o valor total com o frete: R$ {:.2f}".format(valor_total))
    

def main()
   while True:
      try:
        # Entrar valor unitário.
         valor_produto = float(input("Digite o valor unitario do produto: "))
         # Entrar quantidade.
         quantidade_produto = int(input("Digite a quantidade total do produto: "))
      except ValueError or NameError:
         # Avisar usuario que seu input esta incorreto.
         print("Parace que digitou um algo invalido, tente novamente com o preço de um produto desejado!")

      subtotal = valor_produto * quantidade_produto
      frete = calcular_frete(valor_produto, quantidade_produto)
      calcular_valor_total(subtotal, frete)

   

if __name__ == "__main__":
   main()