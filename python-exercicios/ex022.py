#Analisando nomes

nome = str(input('Digite um nome completo: ')).strip()

print('Analisando o seu nome...')
print('Com todas as letras maiusculas: {}'.format(nome.upper()))
print('Com todas as letras minusculas: {}'.format(nome.lower()))
print('o nome possui {} letras no total'.format(len(nome)-nome.count(' ')))
# print('O primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))