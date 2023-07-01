# Faça um programa que leia três números inteiros A, B e C e imprima o maior deles.

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)