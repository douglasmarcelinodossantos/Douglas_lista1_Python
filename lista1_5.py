""" 5. Escreva um programa que recebe uma letra e identifica se ela é consoante. """

letra = input("Você gostaria de saber se uma letra é vogal ou consoante? Então, Informe a letra, por gentileza:  ")

vogal = ['a', 'e', 'i', 'o', 'u']
if letra in vogal:
    print('A letra que você digitou é uma vogal')
else:
    print('A letra que você digitou é uma consoante')