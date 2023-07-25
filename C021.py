# Faça um programa que leia um número inteiro positivo N e imprima a soma dos dígitos desse número. Por exemplo, se a entrada for 358, a saída será 16 (3 + 5 + 8). Obs: Não é permitido transformar os números em strings, ou seja, resolva o problema apenas utilizando operações matemáticas válidas.

N = int(input())

soma = 0

while N != 0:
    primeiro = N % 10
    soma += primeiro
    N = N // 10
print(soma)

