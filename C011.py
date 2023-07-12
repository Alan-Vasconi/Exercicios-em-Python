# Faça um programa que leia um número inteiro e positivo X. Após isso, leia sucessivos números inteiros positivos, até que um número negativo seja lido. Ao fim, escreva o número de vezes que o número inicial X foi lido do usuário.

x = int(input())

contador = 0
while True:
    N = int(input())
    if N == x:
        contador+=1
    if N < 0:
        break
print(contador)
