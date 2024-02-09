salario = float(input('Digite salario: '))
if salario >= 1250:
    nsalario = salario + (salario*10)/100
    print('Aumento de 0.10% R${:.2f}'.format(nsalario))
else:
    nsalario = salario + (salario*15)/100
    print('Aumento de 0.15% R${:.2f}'.format(nsalario))