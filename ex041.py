from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimneto: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação:Sênior')
elif idade > 25:
    print('Classificação: Master')