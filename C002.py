# Faça um programa que leia dois números inteiros positivos X e Y e imprima todos os números de X até Y. Se X for maior que Y, imprima INVALIDO.

X = int(input())
Y = int(input())

if X > Y:
    print('INVALIDO')

while X <= Y:
    print(X)
    X += 1
