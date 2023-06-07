#Um motorista de Uber estipula o preço de uma determinada viagem dada a quantidade de quilômetros percorrida. Para viagens de até X km, é cobrado um valor R$ V1 por km. Acima de Y km, é cobrado o valor R$ V2. Faça um programa que leia X, V1, V2 e a quantidade de quilômetros A da viagem e imprima o valor total com duas casas decimais.

X = float(input())
V1 = float(input())
V2 = float(input())
A = float(input())

if A > X: 
    valor = V2
    valor = V2 * A
    print(f'{valor:.2f}')

else:
    valor = V1
    valor = valor * A
    print(f'{valor:.2f}')