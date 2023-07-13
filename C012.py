# Faça um programa que leia um número inteiro positivo N. Após isso o programa deve ler N números inteiros e ao final da leitura imprimir o maior deles.

n = int(input())
contador = 0
inicial = None
while n > contador:
    x = int(input())

    if inicial == None or x > inicial:
        inicial = x
    else:
        x = inicial
    contador+=1
    
print(x)