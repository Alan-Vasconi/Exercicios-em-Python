# Na matemática, um número primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

# Faça um programa que leia um número inteiro positivo N e imprima 1 se ele for primo e 0 caso contrário.

N = int(input())
valor = 1
divisor = 2
while divisor < N:
    if N % divisor == 0:
        valor = 0
    divisor +=1
if N == 1:
    valor = 0
print(valor)