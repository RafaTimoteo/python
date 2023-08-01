#Números ímpares multiplos de 3

soma = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c  #o mesmo que 'soma = soma + c'
        count += 1 #o mesmo que 'count = count + 1'

print('A soma dos {} números pedidos é igual a {}'.format(count, soma))      