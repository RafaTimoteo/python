#Valor da passagem baseado em km

distancia = float(input('Digite a distancia em km: '))
print('Voce está prestes a começar uma viagem de {}km'.format(distancia))

# if distancia >= 200:
#     taxa = .45 * distancia
# else:
#     taxa = .50 * distancia

taxa = distancia *.45 if distancia >= 200 else distancia * .50 
print('A sua viagem custará R${:.2f}'.format(taxa))