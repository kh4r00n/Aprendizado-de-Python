from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa é: {:.2f}'.format(hi))



'''import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa é: {:.2f}'.format(hi))
'''

'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = (co** 2 + ca** 2) ** (1/2)
print('A hipotenusa é: {:.2f}'.format(hi))'''
