#Cambio monetário#
real = float(input('Digite um valor em R$'))
cot = float(input('Digite o valor do dollar atual US$'))
dollar = (real/cot)
print('Com R${:.2f} é possivel comprar US${:.2f}'.format(real, dollar))
