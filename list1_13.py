""" 13. Escreva um programa que substitua ‘,’ por ‘.’ e ‘.’ por ‘,’ em uma string. Exemplo: 1,000.54
por 1.000,54. """

valor = input('informe uma palavra ou número que você deseja alterar: ')

valor = valor.replace(",", "*").replace(".", ",").replace("*", ".")
print(valor)