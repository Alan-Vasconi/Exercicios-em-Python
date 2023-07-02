# Sejam A, B e C os três lados de um triângulo. Faça um programa que leia o valor de três lados de um triângulo A, B e C. Seu algoritmo deve informar se o triangulo é: Escaleno (todos os lados diferentes); Isósceles (possui dois lados iguais); e Equilátero (todos os lados iguais); Não forma triângulo (quando a soma de dois lados é menor que o terceiro lado).

lado1 = int(input()) # Insere a variavel do lado1 e armazena
lado2 = int(input()) # Insere a variavel do lado2 e armazena
lado3 = int(input()) # Insere a variavel do lado3 e armazena

continuars = True # Condição se vai precisar fazer outras condições

if (lado1 + lado2) < lado3 or (lado1 + lado3) < lado2 or (lado2 + lado3) < lado1: 
# Se o Lado1 + Lado2 < Lado3 ou o Lado1 + Lado3 < Lado2 ou o Lado2 + Lado3 < Lado1 = Invalido e para
    print('INVALIDO')
    continuars = False

elif lado1 == lado2 and lado2 == lado3 and continuars == True:
    # Se o Lado1 for igual o Lado 2 e Lado2 for igual o Lado3 = Equilatero e para a programação
    print('EQUILATERO')
    continuars = False
    
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3 and continuars == True:
    # Se o Lado1 for diferente do que o Lado2 e o Lado2 diferente do Lado3 = Escaleno e para a programação
    print('ESCALENO')
    continuars = False

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 and continuars == True:
    print('ISOSCELES')
    continuars = False
