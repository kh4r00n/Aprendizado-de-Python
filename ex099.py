from time import sleep
def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.2)
        if cont == 0:
            maior =  valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


#Programa Principal
maior(5, 1, 9, 4, 3)
maior(7, 0, 2)
maior(8, 9)
maior(6)
maior()
