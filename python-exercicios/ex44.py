#Forma de pagamento

print(('='*10), 'Lojas Timoteo', ('='*10))
valor = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
      [ 1 ]  à vista dinheiro/cheque
      [ 2 ]  à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
escolha = int(input('Qual opção de pagamento? '))

if escolha == 1:
    desconto = valor - (valor*10/100)
    print('Suas compras de R${:.2f} sairá por R${:.2f} com 10% de desconto.'.format(valor, desconto))
elif escolha == 2:
    desconto = valor - (valor*5/100)
    print('Suas compras de R${:.2f} sairá por R${:.2f} com 5% de desconto.'.format(valor, desconto))
elif escolha == 3:
    print('Suas compras de R${:.2f} sairá por duas parcelas de  R${:.2f} sem juros.'.format(valor, (valor/2)))
elif escolha == 4:
    parcelas = int(input('Em quantas parcelas voce deseja pagar? '))
    if parcelas <= 12:
        ajuste = valor + (valor*20/100) 
        print('Suas compras de R${:.2f} sairá por {:.2f}, dividido em {} parcelas de {:.2f} com juros a 20%.'.format(valor, ajuste, parcelas, (ajuste/parcelas)))
    else:
        print('Não podemos dividir por mais de 12 parcelas')
else:
    print('Opção inválida de pagamento!')        