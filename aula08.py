import os
os.system("cls")
#estrutura de repetição while (enquanto)
#enquanto uma condição for verdadeira ele executou o looping até que ela seja falsa

# aula = 8
# while aula==8:
#     print("silencio!")
#     aula=9
#  else:
#     print("é executado quando o while é falso")

# #while incremental
# i= 0

# while i <10:
#     #i= i+1 #incrementar de 1 em 1
#     i+=1#incremento simplificado mesma coisa que i = i+1
#     print("valor da variável = ", i)


            #ATIVIDADE 1

# i=1
# while i < 18:
#     i+=1
#     print("valor da variável=", i)

            #ATIVIDADE 2

# i=1
# while i > -50:
#     i= i-1
#     print("valor da variável=", i)
   
             #ATIVIDADE3
# print("1- CADASTRAR NOME | 2- CADASTRO CPF | 3- CADASTRO IDADE | 4- SAIR DO PROGRAMA")

# i=0
# opcao= input("digite uma opção:")
# while opcao== "1": 
#     input("digite seu nome:") 
#     if opcao == "2":
#      input("digite seu cpf:") 
#     if opcao == "3":
#      input("digite sua idade:") 
#     else:
#       print("sair do pograma")
    

    #ATIVIDADE SENHA
# senha=1505
# while senha == 1505:
#     senha= int(input("Digite a sua senha:"))
#     if senha == 1505:
#        print("Senha Correta!")
#     elif senha == 9999:
#         print("Programa encerrado!")
#     else:
#         print("Senha Incorreta!")
#         senha = 1505
    
    #ATIVIDADE NUMERO


# import random
# numero=0
# computador= random.randint(1,10)
# while numero != computador:
#     computador= random.randint(1,10)
#     numero = int(input("Digite um número de 1 a 10:"))
#     print(f"Você escolheu:{numero}")
#     print(f"Computador escolheu:{computador}")
#     if numero != computador:
#         print("Numero Incorreto")
#     if numero == computador:
#         print("Numero Correto")


      #CAIXAELETRONICO
# print("-"*10, "MENU", "-"*10)
# print("""
# DIGITE 1 - REALIZAR DEPÓSITO
# DIGITE 2 - REALIZAR SAQUE
# DIGITE 3 - EXTRATO
# DIGITE 4 - SAIR    
#       """)
# print("-"*40)
# saldo= 0
# opcao = ""
# while opcao != 4:
#     opcao= int(input("Digite a opção desejada:"))
#     if opcao == 1:
#        deposito = float(input("Digite o valor do depósito:"))
#        saldo = saldo + deposito
#        print("-"*40)
#     elif opcao == 2:
#        saque= float(input("Digite o valor do saque:"))
#        saldo = saldo - saque
#        print("-"*40)
#     elif opcao == 3 :
#        print(f"SALDO R$:{saldo}")
    #    print("-"*40)
# else:
#    print("Você saiu do programa!")



        #Atividade guanabara
    
# print("-"*10, "MENU", "-"*10)
# print("""
# DIGITE 1 - SOMAR
# DIGITE 2 - MULTIPLICAR
# DIGITE 3 - MAIOR
# DIGITE 4 - NOVOS NÚMEROS
# DIGITE 5 - SAIR DO PROGRAMA 
#       """)
# print("-"*40)


# valor1= float(input("digite um número:"))
# valor2= float(input("Digite outro número: "))
# opcao=0
# print("-"*40)
# while opcao != 5:
#     opcao= int(input("Digite a opção desejada:"))
#     print("-"*40)
#     if opcao == 1:
#         somar= valor1+valor2
#         print(f"Resultado de {valor1} + {valor2} ={somar}")
#         print("-"*40)
#     elif opcao == 2:
#         multiplicar= valor1*valor2
#         print(f"Resultado de {valor1} * {valor2} ={multiplicar}")
#         print("-"*40)
#     elif opcao == 3:
#         maiornumero= max(valor1,valor2)
#         print(f"O maior número é= {maiornumero}")
#         print("-"*40)
#     elif opcao == 4:
#         valor3= float(input("Digite um novo número:"))
#         valor4= float(input("Digite um outro novo número:"))
#         valor1=valor3
#         valor2=valor4
#         print("-"*40)
# else:
#     print("Você saiu do programa!")


           #ATIVIDADE CAIXA ELETRÔNICO
print("-"*18, "CAIXA ELETRÔNICO", "-"*18)
print("CONVERSÃO NOTAS R$: | 100 | 50 | 20 | 10 | 5 | 1 |")
nota=0


