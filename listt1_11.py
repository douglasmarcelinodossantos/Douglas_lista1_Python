""" 11. Escreva uma função que recebe uma lista e organiza os valores em keys e conta a frequência
de cada uma. Por exemplo: a lista [0, 0, 1, 1, 1, 2, 5], resultaria em: {1: 3, 0: 2, 2: 1, 5: 1}. """

lista = [0, 0, 1, 1, 1, 2, 5]

def freq_lista(lista):
    lista = sorted(lista)
    return {i: lista.count(i) for i in lista}

print('A lista [0, 0, 1, 1, 1, 2, 5] organizada por keys e com as respectivas frequências é:')
print (freq_lista(lista))

