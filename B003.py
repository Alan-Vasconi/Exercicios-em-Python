#Faça um programa que leia a idade de um eleitor e imprima se ele é eleitor facultativo (entre 16 e 17 anos), eleitor obrigatório (entre 18 a 69) ou dispensado (acima de 70 ou menor que 16).

idade = int(input())

if idade >= 16 and idade <= 17:
    print('FACULTATIVO')
elif idade >= 18 and idade <= 69:
    print('OBRIGATORIO')

else:
    print('DISPENSADO')