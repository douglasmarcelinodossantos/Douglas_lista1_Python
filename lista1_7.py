""" 7. Escreva um programa que, dada uma lista de números [-2, 34, 5, 10, 5, 4, 32] qualquer,
retorne: o primeiro valor, o número de valores, o último valor, a soma, a média e a mediana.
*** Obs. Para listas com tamanho ímpar, a mediana é o valor do meio, quando ordenada
(sorted()). Para listas pares, retorne os dois valores do meio."""

import statistics

lista = [-2, 34, 5, 10, 5, 4, 32]
lista = sorted(lista)
print(f' A lista ordenada é {lista};')
print(f' o primeiro item da lista é {lista[0]};')
print(f' a lista possui {len(lista)} números;')
print(f' o último item da lista é {lista[-1]};')
print(f' a soma dos itens da lista é {sum(lista)};')

print(f' a mediana da lista é {statistics.median(lista)};')
print(f' finalmente, a média dos itens da lista é {statistics.mean(lista)}.')
