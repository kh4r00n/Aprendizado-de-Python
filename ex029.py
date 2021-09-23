velo = float(input('Qual é a velocidade atual do carro?'))
if velo >80:
    print('Você foi multado! Exccedeu o limite permitido que é de 80km/h')
    multa = (velo-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))

print('Tenha um bom dia! Dirija com segurança!')