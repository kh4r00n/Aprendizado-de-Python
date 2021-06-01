times = ('Bragantino', 'Bahia', 'Ceara', 'Fortaleza', 'Athletico-PR',
         'Flamengo', 'Atletico-GO', 'Sport Recife', 'Juventude', 'Cuiaba',
         'Internacional', 'São Paulo', 'Fluminense', 'Gremio', 'Atletico-MG',
         'America-MG', 'Palmeiras', 'Corinthians', 'Chapecoense', 'Santos')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')