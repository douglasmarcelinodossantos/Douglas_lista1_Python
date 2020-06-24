""" 12. Escreva uma função que liste todos os números primos até 258 (mais o dia do seu
aniversário). Utilize a divisão modular (%). """

meu_aniversario = int(input('Informe o dia do seu aniversário, caso você deseja saber os '
                                'números primos contidos no intervalo compreendido entre 1 e o número 258 '
                                'somado ao dia do seu aniversário: '))


def primos_aniversario (meu_aniversario):
  primos = [2]
  contador = 0
  ultimo_dia = 258 + meu_aniversario
  for i in range (2, ultimo_dia):
    for each in primos:
      if i % each == 0:
        contador = 1
    if contador != 1:
      primos.append(i)

    contador = 0

  primos.append(1)
  primos.append(meu_aniversario)
  primos.sort()

  print ("Os números primos entre 1 e 258 acrescido do seu aniversários estão a seguir:")
  print (primos)

primos_aniversario (meu_aniversario)