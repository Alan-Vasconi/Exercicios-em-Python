# Faça um programa que leia um número inteiro N e imprima a soma de todos os números primos entre 1 e N (inclusive N).

N = int(input())
N2 = 1
import time
final = 0
valor = 1
divisor = 2
contador = 0

resultado = 0
while contador < N:
    if divisor == N2:
        final += N2
    while divisor < N2:
        if N2 % divisor == 0:
            resultado = 0
            break
        else:
            resultado = 1
            divisor +=1
    divisor = 2
    if resultado == 1:
        final += N2
    N2 +=1
    contador +=1
print(final)
