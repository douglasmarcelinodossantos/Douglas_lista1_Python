""" 1. Escreva um programa que imprima o seguinte padrão. """

num = 4
for i in range(num):
    for j in range(i):
        print('* ', end=" ")
    print(' ')

for i in range (num, 0, -1):
    for j in range(i):
        print('* ', end=" ")
    print(' ')