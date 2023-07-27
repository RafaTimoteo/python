#Financiamento imobiliário

valor = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite o salário mensal do comprador: R$'))
anos = int(input('Deseja pagar o financiamento em quantos anos? '))

parcela = valor / (anos * 12)

if parcela <= (salario*(30/100)):
    print('-=-'*20)
    print('SEU FINANCIAMENTO FOI APROVADO!')
    print('-=-'*20)
    print('Voce pagará {} parcelas de R${:.2f}'.format((anos*12), parcela))
elif parcela > (salario*(30/100)):
    print('-=-'*20)
    print('INFELIZMENTE, SEU FINANCIAMENTO NÃO FOI APROVADO.')
    print('-=-'*20)
    print('Tente dividir em mais parcelas.')
