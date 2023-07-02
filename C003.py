# Faça um programa que leia dois números inteiros X e Y e imprima todos os números de X até Y, seguidos nos números de Y até X. Se X for maior que Y, imprima INVALIDO.

X = int(input())
Y = int(input())
valorx = X
if X > Y:
    print('INVALIDO')
while X <= Y:
    print(X)
    X += 1
while X > valorx:
    X -= 1
    print(X)
