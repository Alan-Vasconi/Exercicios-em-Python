#Faça um programa que leia um número inteiro E de eleitores de um município, um número inteiro B que representa o número de votos brancos, um número N de votos nulos e um número V de votos válidos. O programa deve calcular e escrever o percentual que cada um representa em relação ao total de eleitores, além da porcentagem de ausentes. Formate sua saída conforme exemplos abaixo.

E = int(input())
import math

B = int(input())
N = int(input())
V = int(input())

porcentagem = E

resultN = (N *100) / porcentagem
print(f'Nulos: {resultN:.2f}%')

resultB = (B * 100) / porcentagem
print(f'Brancos: {resultB:.2f}%')

resultV = (V * 100) / porcentagem
print(f'Validos: {resultV:.2f}%')

ausentes = E - (N + B + V)

resultA = (ausentes * 100) / porcentagem

print(
    f'Ausentes: {resultA:.2f}%'
)
