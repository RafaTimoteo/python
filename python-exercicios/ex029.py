#Radar de velocidade

velocidade = float(input('Digite a velocidade atual do veículo: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Voce foi multado!')
    print('Voce excedeu o limite de velocidade de 80km/h! Deverá pagar R${:.2f} de multa.'.format(multa))
else:    
    print('Voce está no dentro do limite de velocidade!')
