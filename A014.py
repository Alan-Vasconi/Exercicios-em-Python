#Faça um programa que leia um número inteiro (assuma que esse número terá 4 digitos obrigatoriamente) e inverta esse número. Por fim escreva o número invertido. O seu programa deve apenas manipular números inteiros. Não é permitido usar strings, lista, etc.

numero1 = int(input())

resultado1= numero1 // 1000
resultado2= (numero1 // 100) % 10
resultado3= (numero1 //10) % 10
resultado4= (numero1 % 10)

final = (resultado4 * 1000) + (resultado3 * 100) + (resultado2 * 10) + (resultado1 * 1)
print(final)