# Faça um programa que leia um número inteiro positivo N e imprima "S" se for um número perfeito e "N" caso contrário. Um número é perfeito se for igual à soma de seus divisores positivos diferentes de N. Por exemplo, 6 é perfeito, pois 1 + 2 + 3 = 6.

N = int(input())
contador = 1
soma = 0
while contador < N:
    contador+=1
    if N % contador == 0:
        resultado = N // contador
        if resultado != 0:
            soma += resultado
        if resultado == 1:
            break
if soma == N:
    print('S')
else:
    print('N')