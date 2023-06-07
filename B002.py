#A avenida principal da cidade de Algoritmopolis possui limite de velocidade de L km/h. Se o motorista ultrapassar essa velocidade, é aplicado uma multa de R$ M, mais R$ A por cada km acima do limite. Faça um programa que leia o limite L, o valor da multa M, o valor adicional A e a velocidade V captada pelo radar e informe o valor total da multa. Considere L e V sempre como números inteiros. Apresente a resposta com duas casas decimais.

L = float(input())
M = float(input())
A = float(input())
V = float(input())
valortotal = 0

if L < V:
    excesso = V - L
    multa = excesso * A
    valortotal = M + multa
    print(f'{valortotal:.2f}')

else:
    print(f'{valortotal:.2f}')

