# Faça um programa que leia dois números inteiros positivos A e B e faça o cálculo de multiplicação de A e B usando apenas a operação de soma. Imprima o resultado ao final.

A = int(input())
B = int(input())
inicial = A
inicial2 = B
contador = 1
if B > A or A == B:
    while contador < B:
        A+=inicial
        contador +=1
    print(A)
else:
    while contador <A:
        B+=inicial2
        contador +=1
    print(B)
