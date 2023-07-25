# Considere que seu computador só consegue realizar operações de soma ou subtração, ou seja, está com as operações de divisão e multiplicação inoperantes. Faça um programa que leia dois números inteiros positivos A e B, onde A é a base e B é o expoente de uma potência. Após isso, calcule o valor da potência sem utilizar as operações inoperantes. Imprima o valor de A elevado a B.

# Obs: Não utilize bibliotecas matemáticas. No caso de python, não é permitido usar o operador **. Faça sua solução utilizando laço de repetição.

N = int(input())
pot = int(input())
inicial = 1
contador = 0

if pot == 0:
    print('1')
elif N > 0:
    while pot > 0:
        valor = 0
        for contador in range(N):
            valor += inicial
        inicial = valor
        contador = 0
        pot -=1
    print(inicial)
else:
    print(N)