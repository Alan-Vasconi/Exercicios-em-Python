# Faça um programa que leia dados de temperatura durante uma semana (7 leituras), armazenando em uma lista. Após isso, seu programa deve imprimir quantos dias dessa semana a temperatura esteve acima da média.


maior = 0
contador = 0

N = input().split()
N = [int(valor) for valor in N]
total = sum(N)
tamanho = len(N)
media = total / tamanho
while contador < tamanho:
    if N[contador] > media:
        maior+=1
    contador +=1
print(maior)
