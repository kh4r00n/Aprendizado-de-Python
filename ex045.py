from random import  randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,  2)
print(''' Suas opções:
 [0] Pedra
 [1] Papel
 [2[ Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('Jo')
sleep(1)
print('Ken')
sleep(2)
print('Po!')
sleep(3)
print('-='* 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #Computador jogou Pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Você venceu!')
    elif jogador == 2:
        print('O computador venceu!')
elif computador == 1: #Computador jogou Papel
    if jogador == 0:
        print('O computador venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você Venceu!')
elif computador == 2: #Computador jogou Tesoura
    if jogador == 0:
        print('Você venceu!')
    elif jogador == 1:
        print('Computador Venceu!')
    elif jogador == 2:
        print('Empate')