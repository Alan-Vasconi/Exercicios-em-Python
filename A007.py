#O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está em quilogramas e a altura em metros, ou seja: IMC = massa/altura^2.

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

res = peso / (altura**2)
print(f'{res:.2f}')