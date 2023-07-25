# Faça um programa que leia um conjunto de valores que correspondem as idades de pessoas de uma comunidade. Quando o valor fornecido for um número negativo, significa que não existem mais idades para serem lidas. Após a leitura, seu programa deve informar:

# A média das idades das pessoas (com duas casas decimais)
# A quantidade de pessoas maiores de idade
# A porcentagem de pessoas idosas (considere quem uma pessoa idosa tem mais de 75 anos) (com duas casas decimais)


soma = 0
maior18 = 0
maior75 = 0
media=0
N = int(input())
while N >= 0:
    soma+=N
    media+=1
    if N > 17:
        maior18+=1
    if N >75:
        maior75+=1
    N = int(input())
soma = soma/media
print(f'{soma:.2f}')
print(maior18)
porcentagem = (maior75 * 100) / media
print(f'{porcentagem:.2f}%')