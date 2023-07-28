peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (m): '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Voce está abaixo do peso. IMC: {:.1f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Voce está no peso ideal. IMC: {:.1f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Voce está em sobrepeso. IMC: {:.1f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Voce esta em obesidade. IMC: {:.1f}'.format(imc))
else:
    print('Voce está em obesidade mórbida. IMC: {:.1f}'.format(imc))
