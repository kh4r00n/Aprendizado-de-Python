n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('Tirando {:.2f} e {:.2f} a sua média é: {:.2f} '.format(n1, n2, media))

if media < 5:
    print('REPROVADO')
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('Aprovado')