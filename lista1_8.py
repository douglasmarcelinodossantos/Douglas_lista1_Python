""" 8. Dicionários. Dado o dicionário: d = {‘a’: 0}: faça programas que:
8.1 acrescente um par (chave, valor) {‘b’: 1}, ao dicionário;
8.2 verifique se a key ‘c’ está presente?
8.3 Concatene um dicionário a um outro dicionário: e = {z : 23}. Use o método ‘update’! """

d = {'a': 0}
print(f'O dicionário "d" original é {d}')
d['b'] = 1
print(f'O dicionário "d" acrescentado da chave formada por "b:1" é {d}')
if 'c' in d.keys():
    print('A chave "c" está presente em "d"')
else:
    print('A chave "c" não está presente em "d"')
e = {'z': 23}
d.update(e)
print(f'O dicionário "d" concatenado com o dicionário "e" é representado por {d}')



