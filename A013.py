#Faça um programa que leia um número inteiro S que representa uma quantidade de segundos. Seu programma deve imprimir quatro valores inteiros, que representem a quantidade de segundos S em dias, horas, minutos e segundos. Por exemplo, 188365 segundos representam 2 dias, 4 horas, 19 minutos e 25 segundos. Dica: lembre-se dos operadores resto e divisão inteira.

segundos = int(input())

minutos = segundos // 60
segundos = segundos % 60
horas = minutos // 60
minutos = minutos % 60
dias = horas // 24
horas = horas % 24

print(dias, end = ' ')
print(horas, end = ' ')
print(minutos, end = ' ')
print(segundos)
