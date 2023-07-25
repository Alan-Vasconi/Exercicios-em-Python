# Faça um programa que leia um número inteiro N e imprima a soma de todos os fatoriais entre 0 e N (inclusive N). Não utilize bibliotecas matemáticas.

N = int(input())
inicial = 1
total = 1
contador = 1

while contador <= N:
    inicial *= contador
    total += inicial
    contador +=1
print(total)