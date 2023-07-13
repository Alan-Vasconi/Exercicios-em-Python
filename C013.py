# Faça um programa que leia um número inteiro positivo N. Após isso o programa deve ler N números inteiros e ao final da leitura imprimir o maior, menor e a soma dos números lidos.

N = int(input())
inicial = 0
contador = 0
soma = 0
menor = 0
while contador < N:
    N2 = int(input())
    soma += N2
    if N2 < menor or contador == 0:
        menor = N2
    if N2 > inicial or contador == 0:
        inicial = N2
    contador +=1
print(inicial)
print(menor)
print(soma)
