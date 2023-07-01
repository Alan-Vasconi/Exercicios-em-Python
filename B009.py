# Faça um algoritmo que leia 3 valores inteiros A, B e C. Coloque-os em ordem crescente (ou seja, ao final A deve armazenar o menor valor, C o maior e B o valor do meio). Utilize o modelo abaixo apresentado no final do exercício, modificando apenas o processamento

a = int(input())
b = int(input())
c = int(input())

valorf = 0

if a > b:
    valorf = a
    a = b
    b = valorf
if b > c:
    valorf = b
    b = c
    c = valorf
if a > b:
    valorf = a
    a = b
    b = valorf

    
print(a)
print(b)
print(c)