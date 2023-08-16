# Faça um programa que leia um número inteiro não negativo N e imprima "S" se ele é palíndromo e "N" caso contrário. Um número é palíndromo quando lido da esquerda para a direita é igual ao ser lido da direita para a esquerda. Exemplos: 37173, 1221.

# Obs: Faça seu programa utilizando apenas números inteiros. Não é permitido converter o número para string.


N = int(input())
NO = N
reverso = 0

while N > 0:
    ultimo = N % 10
    reverso = (reverso * 10) + ultimo
    N //= 10

if reverso == NO:
    print("S")  
else:
    print("N")