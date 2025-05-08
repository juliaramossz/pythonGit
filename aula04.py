import os
os.system("cls")

#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)

#ATIVIDADE1
#1-
# idade= float(input("digite sua idade: "))
# if idade >= int(18):
#     print("maior de idade")
# else:
#     print("menor de idade")

# #2-
# if idade < int(0) or idade > int(120) :
#     print("IDADE INVÁLIDA")


# #3-
# email = input("digite seu email: ")
# senha = input("digite a sua senha: ")
# if email == "python@senai.com" and int(12345678):
#     print("USUÁRIO AUTENTICADO")
# else:
#     print("USUÁRIO OU SENHA INVÁLIDOS")






#atividade maça

# print("-"*9, "SUPERMERCADO", "-"*9)
# quantidade= int(input("quantidade de maça: "))

# if quantidade < 12 :
#     calc = quantidade * 0.30
#     print("Você irá pagar (0,30 uni): R$" , calc)
# else:
#     calc = quantidade * 0.25
#     print("Você irá pagar (0,25 uni): R$" , calc)

#ATIVIDADE 1
# print("-"*9, "VOGAL OU CONSOANTE?", "-"*9)
# letra= (input("digite uma letra: "))

# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U": 
#     print("VOGAL") 
# else:
#     print("CONSOANTE")

# ATIVIDADE 2
numero = float(input("digite um número:"))
numero2 = float(input("digite outro número:"))
if numero > numero2 :
    print("numero maior:", numero)
    print("numero menor:", numero2)

else:
    print("numero maior:", numero2)
    print("numero menor:", numero)


