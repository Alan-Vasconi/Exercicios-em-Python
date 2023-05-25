#Em épocas de crise, comerciantes estão oferecendo descontos para aumentarem suas vendas. Faça um programa que leia o valor total da compra e um valor de desconto (de 0 a 100, representando a porcentagem de desconto). O programa de escrever o valor da compra com o desconto aplicado. Escreva a saída com duas casas decimais.

valor = float(input('Digite o valor: '))
desconto = float(input('Digite a porcentagem de desconto: '))

desconto1 = (valor / 100) * desconto
res =  valor - desconto1

print(f'{res:.2f}')