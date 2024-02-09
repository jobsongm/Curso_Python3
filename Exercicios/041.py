from datetime import date
atual = date.today().year
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = atual - ano
if idade <= 9:
    print('Mirim {}'.format(idade))
elif idade <= 14:
    print('Infatil {}'.format(idade))
elif idade <= 19:
    print('Junior {}'.format(idade))
elif idade <= 25:
    print('Senior {}'.format(idade))
else:
    print('Master {}'.format(idade))
