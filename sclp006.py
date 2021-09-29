'''Crie um programa que leia dois valores e printe a divisão inteira e o resto'''

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo número: '))

divint = n1 // n2
resto = n1 % n2

print(f'A divisão inteira de {n1} por {n2} é igual a {divint:.2f}')
print(f'O resto da divisão de {n1} por {n2} é igual a {resto:.2f}')