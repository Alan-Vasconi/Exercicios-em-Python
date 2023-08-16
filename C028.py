# Faça um programa que leia um número inteiro N que indica a quantidade de números em um conjunto. Em seguida, leia os N números inteiros que compõem esse conjunto. O programa deve imprimir o comprimento de um segmento crescente de tamanho máximo. Por exemplo, na sequência [3, 7, 4, 3, 6, 8, 9, 2, 5], o segmento crescente máximo é [3, 6, 8, 9], portanto seu comprimento é 4. Considere que um segmento de tamanho N é crescente quando X1 <= X2 <= ... <= XN.


N = int(input())
L = []
max = 0
inicial = 1
x = 0
contador = 0

while contador < N:
    valor = int(input())
    L.append(valor)
    contador += 1

contador = 1
while contador < N:
    if L[contador] >= L[contador - 1]:
        inicial += 1
    else:
        if inicial > max:
            max = inicial
        inicial = 1
    contador += 1

if inicial > max:
    max = inicial

print(max)
