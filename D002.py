# Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. Em seguida, seu programa deve imprimir os N valores na ordem que foram lidos.


max = int(input())
numeros = input().split()
if len(numeros) <=max:
    format = list(map(int, numeros))
    print(*format)
