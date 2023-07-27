# Faça um programa que leia um número inteiro e positivo N. Após isso leia N números inteiros. Ao fim, imprima 1 se a sequência de números lidos estão ordenados em forma crescente e -1 se estão ordenados de forma decrescente. Se não estão ordenados, imprima 0. Considere que uma sequência de tamanho N é crescente quando X1 <= X2 <= ... <= XN e decrescente quando X1 >= X2 >= ... >= XN. No caso desse exercício, se todos os valores lidos forem iguais, considere como um segmento crescente.

N = int(input())
L = []

crescente = True
contrario = True
contador = 0

while contador < N:
    numero = int(input())
    L.append(numero)
    contador +=1
contador = 0

while contador < N:
    if contador>0:
        if L[contador] < L[contador-1]:
            crescente = False
        if L[contador] > L[contador-1]:
            contrario = False
    contador +=1

if crescente == True:
    print(1)
elif contrario == True:
    print(-1)
else:
    print(0)