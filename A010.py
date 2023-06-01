#Faça um programa que leia uma temperatura em graus Celsius e converta e escreva o correspondente em graus Fahrenheit (pesquise como essa conversão é feita).

celsius= float(input())

conv = celsius * (9/5) + 32
print(f'{conv:.2f}')
