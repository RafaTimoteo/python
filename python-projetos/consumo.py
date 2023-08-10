print('='*41)
print('= Calculadora de consumo de combustível =')
print('='*41)

conumo = int(input('Digite quantos km/L o veículo faz: '))
percuso = float(input('Digite a distância percorrida em km: '))
preco = float(input('Digite o valor do litro do combustível: R$'))
gasto = percuso/conumo
total = (gasto*preco)

print('='*41)
print('O veículo consumiu {:.2f}L ou {:.0f}ml para fazer o trajeto.'.format(gasto, (gasto*1000)))
print('Com o combustível a R${:.2f}/L, a viagem custa R${:.2f}'.format(preco, total))