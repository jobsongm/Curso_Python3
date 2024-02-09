preco = float(input('Informe o valor da compra R$'))
print('Forma de pagamento')
print('[ 1 ] avista dinheiro ou cheque')
print('[ 2 ] avista cartão')
print('[ 3 ] 2x cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    print('Valor com 10% de desconto R${:.2f}'.format(preco-(preco*10/100)))
elif opcao == 2:
    print('Valor com 5% desconto R${:.2f}'.format(preco-(preco*5/100)))
elif opcao == 3:
    print('Valor em 2x de {:.2f} total de {:.2f}'.format(preco/2,preco))
elif opcao == 4:
    parcelas = int(input('Informe a quantidade de parcelas: '))
    print('Parcelas serão de {:.2f} com 20% de juros, total de {:.2f}'.format((preco+(preco*20/100))/parcelas,preco+(preco*20/100)))
else:
    print('Opção invalida!')