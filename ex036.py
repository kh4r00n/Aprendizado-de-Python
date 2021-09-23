casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salario?'))
anos = int(input('Em quantos anos pretende pagar?'))
prestação = casa / (anos * 12)
minimo = salario * 30/100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end ='')
print(' a prestação sera de {:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo aprovado')
else:
    print('Emprestimo negado')
