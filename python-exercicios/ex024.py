# Cidade começa com santo

cidade = str(input('Digite o nome de um cidade: ')).strip()

# lista = cidade.split()
# print('Começa com o nome "Santo"? {}'.format('SANTO' in lista[0].upper()))

print('Começa com o nome "Santo"? {}'.format((cidade[:5].upper() == 'SANTO')))