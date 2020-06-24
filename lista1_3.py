""" 3. Escreva um programa que corre os números de 23 a 83 e imprime. Mas, quando for múltiplo
de três, imprima ‘Pum’, quando for múltiplo de 5 imprima ‘Bla’, quando for de ambos
imprima ‘PumBla’. """

# Imprimindo um intervalo de números entre 23 e 83, substituindo alguns números por strings
for i in range(23, 84):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print('PumBla')
    elif i % 3 == 0:
        print('Bla')
    elif i % 5 == 0:
        print('Pum')




