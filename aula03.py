import os
os.system("cls")

#continuação Input com Int e Float
#int() -> converte para inteiro
#float() -> converte para n quebrado

# numero = 10
# numero2 = input("digite um numero: ")
# print("o tipo de número é,", type(numero2)) 
# soma = numero + int(numero2) 
# print(f"soma de {numero} + {numero2}  = ", soma)

#exemplo2
# num1 = input("digite um número: ")
# soma = float(num1) + 15
# print("A soma de ",num1 , "+", "15" ,"=", soma)

#exemplo3
# n1 = float(input("digite um número: "))
# n2 = float(input("digite outro numero: "))

# soma = n1+n2

# print(f"a soma de {n1} + {n2} = ", soma)

#exercício 1
# numero1 = input("digite um número: ")
# numero2 = input("digite outro número: ")
# multiplicaçao= int(numero1)*int(numero2)
# print(f"A multiplicaçao de {numero1} * {numero2} é =", multiplicaçao)

# #Exercício 2
# numero1 = input("digite um número: ")
# antecessor = int(numero1)-int(1)
# sucessor = int(numero1)+int(1)
# print(f"O antecessor de {numero1} é", antecessor)
# print(f"O sucessor de {numero1} é", sucessor)

# #exercício 3
# numero1 = input("digite um ano: ")
# idade = int(2025)-int(numero1)
# print(f"Você tem {idade} anos")



#exercício supermercado
#round(valor,qtdCasasDecimais) -> faz o arredondamento dos valores

print("-"*9 , "SUPERMERCADO" , "-"*9)
nomedoproduto = input("digite o nome do produto: ")
preçodoproduto = input("digite o preço do produto R$: ")
nomedoproduto2 = input("digite o nome do produto: ")
preçodoproduto2 = input("digite o preço do produto R$: ")
print("-"*11 , "CAIXA" , "-"*11)
desconto = int(preçodoproduto)-0.10*int(preçodoproduto)
print(f"{nomedoproduto} custa R${preçodoproduto} com 10% de desconto =",desconto)
desconto2 = int(preçodoproduto2)-0.25*int(preçodoproduto2)
print(f"{nomedoproduto2} custa R${preçodoproduto2} com 25% de desconto =",desconto2)
print("-"*38)
total = int(desconto)+int(desconto2)
print(f"TOTAL R$ =",total)
