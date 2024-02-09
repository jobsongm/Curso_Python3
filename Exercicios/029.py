velocidade = float(input('Qual foi a velocidade? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Velocidade ultrapassada a multa é de R${:.2f}'.format(multa))
else:
    print('Velocidade permitida parabens!')