""" 9. Escreva uma função que faz um loop sobre as keys de um dicionário. Se as keys forem
vogais, eleve o valor ao quadrado. Caso contrário, set o valor para 0. Use if k in ‘aeiou’."""

dicionario = {'a': 5, 'b': 10, 'e': 15, 'c': 20, 'i': 25, 'd': 30, 'o': 35, 'f': 40, 'u': 45, 'g': 50}

def funcao_dicionario(dicionario):
  for each in dicionario:
    if each in 'aeiou':
      dicionario[each] = dicionario[each] ** 2
    else:
      dicionario[each] = 0

  print('Ao elevarmos os valores das keys que são vogais ao quadrado e imprimirmos "zero" para os valores das consoantes'
      ' obtemos o seguite dicionário:')

  print(dicionario)

funcao_dicionario(dicionario)



