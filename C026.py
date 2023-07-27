# Ana gosta muito de matemática e de brincar com números. Ela definiu o conceito de "Número da Ana. Se um número inteiro não negativo N é produto de três números inteiros consecutivos então N é um "Número da Ana".
# Faça um programa que leia um número inteiro não negativo N e imprima "S" se for um "Número da Ana" e "N" caso contrário. Por exemplo, 120 é um "Número da Ana", pois é resultado da multiplicação 4 x 5 x 6.

N = int(input())
contador = 0
condicao = False
while contador <N and condicao == False:
    contador +=1
    variavel1 = contador
    variavel2 = contador+1
    variavel3 = variavel2 +1
    soma1 = contador * (variavel2)
    soma2 = soma1 * (variavel3)
    if soma2 == N:
        condicao = True
    soma1 = 0
    soma2 = 0
if condicao == True:
    print('S')
else:
    print('N')
    