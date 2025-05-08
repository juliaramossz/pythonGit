import os
os.system("cls")
  #IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
  #ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA
  #:.2f -> formata para 2 casas decimais apenas no fstring


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


   # ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


  # NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


   # SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# idade = int(input("digite sua idade: "))
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


    #ATIVIDADE MÉDIA
# nota1 = float(input("digite a 1 nota:").replace(",","."))
# nota2 = float(input("digite a 2 nota:").replace(",","."))
# media = (nota1+nota2)/2
# print(f"Sua nota final é =", media)
# if media > 7 :
#     print("Aprovado")
# elif media <= 7 and media >= 5 :
#     print("Em recuperação")
# elif media < 5 :
#     print("Reprovado")

    #ATIVIDADEIMC
# peso= float(input("digite o seu peso:"))
# altura= float(input("digite a sua altura:"))
# imc = float(peso / (altura * altura))

# print(f"seu imc é {imc:.2f}")

# if imc <= 17 :
#     print("Muito abaixo do peso")
# elif imc > 17 and imc < 18.49:
#     print("Abaixo do peso")
# elif imc > 18.5 and imc < 24.99:
#     print("Peso normal")
# elif imc > 25 and imc < 29.99:
#     print("Acima do peso")
# elif imc > 30 and imc < 34.99:
#     print("Obesidade 1")
# elif imc > 35 and imc < 39.99:
#     print("Obesidade 2")
# else:
#     print("Obesidade 3(mórbida)")

   #ATIVIDADE AUTOCAR
print("-"*9 , "REAJUSTE AUTOCAR" , "-"*9)

print(r"""

                       ____________________                              
                     //|           |        \                            
                   //  |           |          \                          
      ___________//____|___________|__________()\__________________      
    /__________________|_=_________|_=___________|_________________{}    
    [           ______ |           | .           | ==  ______      { }   
  __[__        /##  ##\|           |             |    /##  ##\    _{# }_ 
 {_____)______|##    ##|___________|_____________|___|##    ##|__(______}
             /  ##__##                              /  ##__##        \   

    """)

print("-"*20)
print("TABELA DE REAJUSTE DE SALÁRIO")
print("Salários entre R$2799.99: aumento de de 20%")
print("Salários entre R$2800.00 e R$6999.99 : aumento de de 15%")
print("Salários entre R$7000.00 e R$6999.99 : aumento de de 10%")
print("Salários entre R$15000.00 : aumento de de 5%")

print("-"*20)

salário = float(input("digite seu salário R$:"))
print("Salário sem reajuste R$:", salário)

if salário < 2799.99 :
    print("O percentual da sua faixa é:20%")
elif salário >2800.00 and salário <6999.99 :
    print("O percentual da sua faixa é:15%")
elif salário > 7000.00 and salário >14999.99:
    print("O percentual da sua faixa é:10%")
else:
    print("O percentual da sua faixa é:5%")


if salário < 2799.99 :
    print("Aumento de:", 0.20 * salário)
elif salário >2800.00 and salário <6999.99 :
    print("Aumento de:", 0.15 * salário)
elif salário > 7000.00 and salário >14999.99:
    print("Aumento de:", 0.10 * salário)
else:
    print("Aumento de:", 0.05 * salário)

if salário < 2799.99 :
    print("Novo salário", salário * 0.20 + salário)
elif salário >2800.00 and salário <6999.99 :
    print("Novo salário", salário * 0.20 + salário)
elif salário > 7000.00 and salário >14999.99:
    print("Novo salário", salário * 0.20 + salário)
else:
    print("Novo salário", salário * 0.20 + salário)
