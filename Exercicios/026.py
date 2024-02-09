frase = str(input('Digite um nome: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('O primeiro A aparece na posição {}'.format(frase.find('A')+1))
print('O ultimo A aparece na posição {}'.format(frase.rfind('A')+1))