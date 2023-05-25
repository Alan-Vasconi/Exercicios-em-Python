#Faça um programa que leia dois números inteiros. Após isso, seu programa deve imprimir o resultado das seguintes operações: 1) o valor da divisão real do primeiro número lido pelo segundo (imprimir com duas casas decimais); 2) o valor da divisão inteira do primeiro pelo segundo (imprimir como número inteiro); 3) o valor do resto da divisão do primeiro pelo segundo (imprimir como número inteiro).#


valor1 = int(input('Digite o valor 1:'))
valor2 = int(input('Digite o divisor: '))

res1 = valor1 / valor2
print(f'{res1:.2f}')
res2 = valor1 // valor2
print(res2)
res3 = valor1 % valor2
print(res3)