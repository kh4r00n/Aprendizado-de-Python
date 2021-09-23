n1 = float(input('Digite a altura da parede'))
n2 = float(input('Digite a largura da parede'))

a = n1 * n2
b = a / 2

print('Será necessário {:.2f} litros de tinta para pintar uma parede com {:.2f} m2'.format(b, a))

