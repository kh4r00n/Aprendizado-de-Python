passagem = float(input('Qual a distância em km da sua viagem?'))

if passagem <=200:
    p1 = passagem * 0.50
    print('A sua passagem custa {:.2f} R$'.format(p1))
else:
    p2 = passagem * 0.45
    print('A sua passagem custa {:.2f} R$'.format(p2))

