# Faça um programa que leia dois números inteiros não negativos A e B, onde A é a base e B é o expoente de uma potência. Após isso, calcule e imprima o valor de A elevado a B. Não utilize bibliotecas matemáticas. No caso de python, não é permitido usar o operador **. Faça sua solução utilizando laço de repetição.

numero = int(input())
expoente = int(input())

valor = 1
contador = 1
if expoente != 0:
    while contador <= expoente:
        valor = valor * numero
        contador += 1

print(valor)
