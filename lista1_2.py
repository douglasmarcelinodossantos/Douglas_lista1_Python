""" 2. Altere o programa "lista1_.py" para que o usuário possa entrar com o número máximo de estrelas."""

num = int(input('Informe um número de asteriscos que você deseja na maior linha de um triângulo de asteriscos: '))


for i in range(num):
    for j in range(i):
        print('* ', end="")
    print(' ')

for i in range(num,0,-1):
    for j in range(i):
        print('* ', end="")
    print(' ')