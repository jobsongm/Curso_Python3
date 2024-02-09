count = 0
soma = 0
for c in range(0,6):
    n = int(input(''))
    if n % 2 == 0:
        soma += n
        count += c
print(soma)
