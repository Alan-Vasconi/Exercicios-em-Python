# Faça um programa que leia uma sequência de números inteiros do usuário até que ele digite o valor zero. Quando o valor zero for digitado, o programa deve imprimir o resultado em três linhas: 1ª linha) Soma dos valores pares da sequência; 2ª linha) Soma dos valores ímpares da sequência; 3ª linha) soma de todos os valores da sequência.

N = 1
pares = 0
impares = 0
while N != 0:
    N = int(input())
    if N %  2 == 0:
        pares += N
    else:
        impares += N
print(pares)
print(impares)
print(pares + impares)
