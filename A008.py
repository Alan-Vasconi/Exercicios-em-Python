#Faça um programa que leia o valor dos catetos de um triângulo retângulo e calcule a hipotenusa, de acordo com o Teorema de Pitágoras. Pesquise como extrar a raiz quadrada de um número.

cateto1 = float(input('Digite o cateto 1: '))
cateto2 = float(input('Digite o cateto 2: '))

hip = (cateto1**2) + (cateto2**2)
hip = hip ** (1/2)

print(f'{hip:.2f}')