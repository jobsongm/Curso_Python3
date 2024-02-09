frase = str(input('Digite uma frase: ')).strip().upper()
print('Você digitou a frase {}'.format(frase))
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palidromo')
else:
    print('A frase digitda não é um palidromo!')