""" 10. Escreva uma função que retorna os máximos e mínimos de um dicionário. """

dicionario = {'a': 5, 'b': 10, 'e': 15, 'c': 20, 'i': 25, 'd': 30, 'o': 35, 'f': 40, 'u': 45, 'g': 50}

def max_min_valor(dicionario):
    print(f'O valor máximo do dicionário é: {max(dicionario.values())}')
    print(f'O valor mínimo do dicionário é: {min(dicionario.values())}')

max_min_valor(dicionario)




