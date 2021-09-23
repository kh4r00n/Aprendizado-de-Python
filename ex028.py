from random import randint
from time import sleep

computador = randint(0, 5) # faz o computador 'pensar'
'''print('Pensei no número {}'.format(computador)) '''
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei?'))
print('Processando...')
sleep(2)
if jogador == computador:
    print('Parabens arrombado')
else:
    print('Ganhei. Eu pensei no número {} e não no {}!'.format(computador, jogador))
