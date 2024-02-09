import random
n1 = str(input('Digite primeiro nome '))
n2 = str(input('Digite segundo nome '))
n3 = str(input('Digite terceiro nome '))
n4 = str(input('Digite quarto nome '))
nomes = [n1,n2,n3,n4]
random.shuffle(nomes)
print(nomes)