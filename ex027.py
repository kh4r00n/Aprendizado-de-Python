n = str(input('Digite seu nome')).strip()
nome = n.split()
print('Seu primeiro nome é:{}'.format(nome[0]))
print('Seu último nome é:{}'.format(nome[len(nome)-1]))
