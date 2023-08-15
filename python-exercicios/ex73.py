# Tabela do brasileirão

time = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 
        'Bragantino', 'Fluminense', 'Athletico-PR', 'Cuiabá',
        'São Paulo', 'Atlético-MG', 'Fortaleza', 'Cruzeiro',
        'Internacional', 'Corinthins','Goiás', 'Bahia', 'Santos',
        'Coritiba', 'Vasco', 'América-MG')

print('-=-'*20)

print(f'Os primeiros 20 colocados do Canpeonato brasileiro: {time}')

print('-=-'*20)

print(f'Os 5 primeiros colocados {time[:5]}')

print('-=-'*20)

print(f'Os últimos 4 colocados: {time[-4:]}')

print('-=-'*20)

print(f'Em ordem alfabética: {sorted(time)}')

print('-=-'*20)

print('O Fortaleza está na {}ª posição'.format((time.index('Fortaleza'))+1))\

print('-=-'*20)
