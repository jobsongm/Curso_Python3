from datetime import date
atual = date.today().year
ano = int(input('Digite ano de nascimento: '))
idade = atual - ano
if idade < 18:
    print('Alistamento ainda não obrigatorio {} anos falta {} anos para alistamento'.format(idade,18-idade))
elif idade > 18:
    print('Alistamento passou do prazo {} anos, passou {} anos'.format(idade,idade-18))
else:
    print('Alistamento na dada correta {} anos'.format(idade))