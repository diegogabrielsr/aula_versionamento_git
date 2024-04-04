# utilizado para importar a biblioteca math para uso do math.pi
import math
# mensagem de boas vindas para o usuario 
print("Seja Bem vindo a Calculadora de Perimetro e Area de uma circuferencia no Python!!")
# função usada para determinar o Menu do desafio de Codigo
def menu():
  # mensagem para o usuario saber usar o codigo
    print(" Digite o valor do Raio para iniciar E depois escolha a operação necessaria")
    #entradas de dados, inserção do valor do Raio
    raio = float(input("insira o o valor do Raio do Circulo: "))
    #estrutura de validação com while True
    while True:
      #mensagens para orientar o uso do codigo
      print("Selecione a operação desejada abaixo!:")
      print( "Digite '1' Para calcular a área do circulo: ")
      print( "Digite '2' Para calcular o Perimetro do circulo: ")
      print( "Digite '3' Para retornar ao  Menu Inicial: ")
      #variavel para logica das condições do menu
      opcao = input("escolha a opção do menu: ")
      #condições para funcionamento do menu
      if opcao == '1':
        calculo_area(raio)
      elif opcao == '2':
        calculo_perimetro(raio)
      else:
         menu()
#função responsavel por calcular a area
def calculo_area(raio):
   area = math.pi * raio **2 
   print(f"area do circulo é : {area:.2f}")
   return area
#função responsavel por calcular o perimetro
def calculo_perimetro(raio):
   perimetro = 2 * math.pi * raio 
   print(f"a area do perimetro do circulo é: {perimetro:.2f}" )
   return perimetro

menu()
'''area, perimetro = calculo_circulo(raio)'''





