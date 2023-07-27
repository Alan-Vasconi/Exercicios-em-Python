# Faça um programa que leia um número inteiro N que indica a quantidade de números em um conjunto. Em seguida, leia os N números inteiros que compõem esse conjunto. Por fim, o programa deve imprimir dois números, que representam os dois maiores valores encontrados no conjunto, ordenados de forma decrescente.


quantidade = int(input())
contador = 1
N = int(input())

maior = N
maiormen = 0

while contador < quantidade:
    N = int(input())
    contador +=1
    if N > maior:
        maiormen = maior
        maior = N
    elif N > maiormen:
        maiormen= N
if maior > maiormen:
    print(maior)
    print(maiormen)
else:
    print(maiormen)
    print(maior)
    