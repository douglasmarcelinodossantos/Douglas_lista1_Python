""" 4. Escreva um programa que ache e imprima os números divisíveis por 13 e por 19, entre o ano
de nascimento da sua mãe e 2727. """

print('Você gostaria de saber os anos dentro de um intervalo composto pelo ano de nascimento de'
                         ' sua mãe e o ano de 2727 e que seriam divisíseis por 13 e 19?')

ano_nasc_mae = int(input('Então, informe o ano de nascimento da sua mãe: '))

for i in range(ano_nasc_mae, 2728):
    if i % 13 == 0 and i % 19 == 0:
        print(i)