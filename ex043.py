peso = float(input('Qual é seu peso?(kg)'))
altura = float(input('Qual a sua altura?(m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')
elif imc <= 25:
    print('Peso Ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')
