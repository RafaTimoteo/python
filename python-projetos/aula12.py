nome = str(input('Qual  é seu nome? ')).strip()

if nome.lower() == 'rafael':
    print('Que nome bonito!')
elif nome.lower() == 'pedro' or nome.lower() == 'gabriel' or nome.lower() == 'joão Victor':
    print('Seu nome é muito comum no Brasil!')
elif nome.lower() in 'ana cláudia jéssica juliana':
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal')

print('Prazer em conhecer {}!'.format(nome))