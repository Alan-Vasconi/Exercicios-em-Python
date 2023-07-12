# Faça um programa que leia dois números inteiros e imprima o máximo divisor comum (MDC) entre eles. Dica: pesquise sobre o algoritmo de euclides.

Numero1 = int(input())
Numero2 = int(input())
sobra1 = 0
contador = 0
fatormax = max(Numero1,Numero2)
while Numero2 != 0 and contador < fatormax:
    sobra1 = Numero1 % Numero2
    Numero1 = Numero2
    Numero2 = sobra1
    contador +=1
    if Numero2 == 0:
        print(Numero1)
