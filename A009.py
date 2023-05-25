#Faça um programa que leia três números reais A, B e C de uma equação do segundo grau, considerando: Ax^2 + Bx + C. Seu programa deve calcular e imprimir as as raízes da equação. Assuma que delta sempre será positivo.

a=float(input('Digite o valor A: '))
b=float(input('Digite o valor B: '))
c=float(input('Digite o valor C: '))

delta1 = b**2
delta2 = (4 * a) * c
delta3 = delta1 - delta2

raizdelta = delta3 ** (1/2)
raiz1 = (-b + raizdelta) / (2*a)
raiz2 = (-b - raizdelta) / (2*a)

raiz1 = f'{raiz1:.2f}'
raiz2 = f'{raiz2:.2f}'

print(raiz1)
print(raiz2)