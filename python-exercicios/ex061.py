# Progreção Aritmética (estrutura 'while')

print('-=-'*15)
print('PROGRESSÃO ARITMÉTICA')
print('-=-'*15)

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da progreção: '))
term = p
c = 1

while c <= 10:
  print('{}'.format(term), end=' > ')
  term = term + r
  c = c + 1

print('FIM')