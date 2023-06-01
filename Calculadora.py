# PROJETO 1: CALCULADORA
# Introdução:
# A calculadora é um projeto clássico em Python que permite aos usuários realizar operações básicas de matemática, como adição, subtração, multiplicação e divisão. Neste projeto, você aprenderá a lidar com entrada do usuário, operações matemáticas básicas e formatação de saída.

#O QUE FAZER:

# Crie um loop para que o usuário possa realizar várias operações, se desejar. Por exemplo, você pode usar um loop while que continua executando até que o usuário escolha sair do programa.
while True:

#Crie um programa que receba duas variaveis de referencia para a calculadora:
  primeiroDigito = float(input("Digite o primeiro numero: "))
  segundoDigito = float(input("Digite um segundo numero: "))

# Crie um menu inicial que exiba as opções disponíveis para o usuário: adição, subtração, multiplicação e divisão.
# Solicite ao usuário que escolha uma das opções do menu.
  operacao = int(input("Qual seria a operação?\n1 = -\n2 = + \n3 = /\n4 = X\nDigite o numero da operação:"))
  
  # Realize a operação matemática correspondente com os números fornecidos pelo usuário.
    
  if operacao == 1:  
  # Apresente o resultado da operação de forma clara e formatada.
    print(f"{primeiroDigito} - {segundoDigito} = {primeiroDigito-segundoDigito}")

  elif segundoDigito == 0 and operacao == 3:
  #Trate casos especiais, como divisão por zero. Se o usuário selecionar a opção de divisão e o segundo número for zero, você deve exibir uma mensagem adequada para informar que a operação não é possível.
    print("Valor invalido") 
    
  elif operacao == 2:    
  # Apresente o resultado da operação de forma clara e formatada.
    print(f"{primeiroDigito} + {segundoDigito} = {primeiroDigito+segundoDigito}")
  elif operacao == 3:    
  # Apresente o resultado da operação de forma clara e formatada.
    print(f"{primeiroDigito} / {segundoDigito} = {primeiroDigito / segundoDigito}")
  elif operacao == 4:    
  # Apresente o resultado da operação de forma clara e formatada.
    print(f"{primeiroDigito} X {segundoDigito} = {primeiroDigito*segundoDigito}")     
  # Lembre-se de tratar casos de erro, como divisão por zero ou entrada inválida.
  else:
   print("Entrada invalida")
  #Forneça uma opção para o usuário sair do programa. Por exemplo, você pode adicionar uma opção no menu para encerrar o loop e encerrar o programa.
  parar = input("\nDigite 'parar' para encerrar a calculadora digite qualquer outra coisa para retornar a calculadora:  ").upper().strip()
  
  if parar == "PARAR":
    break
print("\nCalculadora encerrada")
  
  