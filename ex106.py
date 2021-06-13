

def ajuda(com):
    help(com)



def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp',1)
    comando = str(input("Função ou Biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!', 1)