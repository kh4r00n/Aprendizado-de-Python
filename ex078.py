listan = []
mai = 0
men = 0
for c in range(0, 5):
    listan.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listan[c]
    else:
        if listan[c] > mai:
            mai = listan[c]
        if listan[c] < men:
            men = listan[c]
print('=-' * 30)
print(f'Você digitou os valores{listan}')
print(f'O maior valor digitado foi {mai} nas posições: ', end='')
for i, v in enumerate(listan):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições: ', end='')
for i, v in enumerate(listan):
    if v == men:
        print(f'{i}...', end='')
print()

