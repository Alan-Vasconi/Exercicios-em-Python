# Faça um programa que leia dois números inteiros N e M e imprima a soma de todos os números entre eles (inclua N e M na soma). Faça sua solução utilizando laço de repetição.

N = int(input())
M = int(input()) 


if M > N:
    maior = M
    menor = N
    contador = M - N
elif N > M:
    maior = N
    menor = M
    contador = N - M
resultado = menor
while contador != 0:
    menor = menor+1
    resultado +=  menor
    contador -= 1


print(resultado)