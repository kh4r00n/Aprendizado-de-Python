salario = int(input('Digite o valor do seu salário:'))

if salario > 1250:
    novo = salario + (salario * 10/100)
if salario <= 1250:
    novo = salario + (salario * 15/100)
print('O seu salário agora é: {}'.format(novo))
