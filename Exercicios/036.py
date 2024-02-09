casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salario? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
parcela = casa / (anos*12)
minimo = salario*30/100
print('Para pagar uma cara de R${:.2f} em {} anos'.format(casa,anos))
print('O valor da parcela sera R${:.2f}'.format(parcela))
if parcela <= minimo:
    print('Emprestimo Aprovado')
else:
    print('Emprestimo Negado')