# Progreção Aritmética melhorada (estrutura 'while')

print('-=-'*15)
print('PROGRESSÃO ARITMÉTICA')
print('-=-'*15)

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da progreção: '))
term = p
c = 1
total = 0
more = 10


while more != 0:
    total = total + more
    while c <= total:
        print('{}'.format(term), end=' > ')
        term = term + r
        c = c + 1
    print('PAUSA')
    more = int(input('Quantos termos a mais deseja mostrar: '))

print('Programa finalizado com {} termos mostrados'.format(c))