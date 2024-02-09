a = int(input('Digite numero: '))
b = int(input('Digite numero: '))
c = int(input('Digite numero: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c>b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor {}'.format(menor))
print('O maior valor {}'.format(maior))