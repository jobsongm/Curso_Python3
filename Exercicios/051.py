termo = int(input('Termo '))
pa = int(input('PA '))
decimo = termo + (10-1)*pa
for c in range(termo,decimo,pa):
    print(' {}'.format(c), end=' -> ')
print('Acabou')