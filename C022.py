# Você está na Austrália treinando cangurus para se locomoverem em linha reta. Você quer saber se dois cangurus estarão na mesma posição em um determinado tempo, dado a posição inicial de cada canguru e qual a distância que eles saltam. Como você sabe programar muito bem, você decidiu fazer um programa para isso. Seu programa deve ler:

# A posição inicial X1 e a distância do pulo V1 do primeiro canguru.
# A posição inicial X2 e a distância do pulo V2 do segundo canguru.

# Após isso, seu programa deve imprimir SIM se os dois cangurus se encontrarão no mesmo ponto e NAO caso eles nunca se encontrem.

# Por exemplo, o primeiro canguru começa em X1 = 2 e tem uma distância do pulo de V1 = 1. O segundo canguru começa em X2 = 1 e tem uma distância de pulo de V2 = 2. Após um pulo ambos estarão no ponto 3, portanto a respota é SIM.

Canguru1 = int(input())
Pulo1 = int(input())
Canguru2 = int(input())
Pulo2 = int(input())

resposta = 2

while resposta == 2:
    if Canguru1 == Canguru2:
        resposta = 1
    elif (Canguru1 > Canguru2 and Pulo1 >= Pulo2) or (Canguru1 < Canguru2 and Pulo1 <= Pulo2):
        resposta = 0
    else:
        diferenca = abs(Canguru1 - Canguru2)
        if diferenca % abs(Pulo1 - Pulo2) == 0:
            resposta = 1
        else:
            resposta = 0

if resposta == 1:
    print('SIM')
else:
    print('NAO')
