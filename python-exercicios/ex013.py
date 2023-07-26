#Reajuste de salário#
s = float(input('Qual é o salario atual? R$'))
sfinal = float(s+(s*15/100))
print('Com acréscimo de 15%, o salário será R${:.2f}'.format(sfinal))