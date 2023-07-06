# Faça um programa que leia um número natural N e imprima o número harmônico de ordem N. Um número harmônico H é definido por:

# H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N

# Imprima o resultado com 4 casas decimais.

N = int(input())

N = 1/N
x = 1
valor = 0
while (1/x) != N:
    x += 1
    valor += (1/x)

valor += 1
valor = (f'{valor:.4f}')
print(valor)