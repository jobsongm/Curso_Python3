peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em Metros: '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Abaixo do peso {:.1f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Peso ideal {:.1f}'.format(imc))
elif 25 <= imc < 30:
    print('Sobre peso {:.1f}'.format(imc))
elif 30 <= imc < 40:
    print('Obesidade {:.1f}'.format(imc))
else:
    print('Obesidade Morbida {:.1f}'.format(imc))