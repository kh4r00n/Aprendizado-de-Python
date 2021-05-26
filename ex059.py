from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''     [1] Somar
     [2] Multiplicar
     [3] Maior
     [4] Novos números
     [5] Sair do programa''')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a: {}'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1 * n2
        print('A multiplicação de {} x {} é igual a: {}'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é: {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente Novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa. Volte sempre.')