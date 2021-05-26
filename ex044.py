print('{:=^40}'.format('Lojas Americanas'))
preço = float(input('Digite o preço das compras: '))
print('''Formas de Pagamento
[1] á vista dinheiro/cheque
[2]á vista cartão
[3]2x no cartão
[4]3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))

if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc

    print('Sua compra sera parcelada em {:.2f} de {:.2f} com juros'.format(totparc, parcela))
else:
    total = preço
    print('Opção inválida de pagamento. Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preço,total))
