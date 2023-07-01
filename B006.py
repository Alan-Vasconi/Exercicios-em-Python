# Faça um programa que leia os coeficientes a, b e c de uma equação do segundo grau ax² + bx + c. Após isso, calcule e imprima a soma das raízes da equação. Se as raízes não forem reais, imprima nan (use print(math.nan))

a = float(input())
b = float(input())
c = float(input())
import math

delta1 = b**2
delta2 = (4 * a * c)
delta3 = delta1 - delta2

if delta3 < 0:
    print(math.nan)

else:
    raiz2 = (-b + (delta3 ** (1/2)))
    raiz3= raiz2 / (2*a)
    raiz4 = (-b - (delta3 ** (1/2)))
    raiz5 = raiz4/ (2*a)
    resultado = raiz3 + raiz5
    print(f'{resultado:.2f}')
    
