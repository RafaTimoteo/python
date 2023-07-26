#Analisando Triangulos

print('-=-'*20)
print('ANALISADOR DE TRIANGULOS')
print('-=-'*20)


a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('É possivel formar um tringulo com essas retas')
else:
    print('Não é possivel formar um triangulo com essas retas')