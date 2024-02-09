n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
nota = (n1+n2)/2
if nota >= 7:
    print('Aluno Aprovado {}'.format(nota))
elif nota >= 5 and nota <= 6.9:
    print('Aluno em Recuperação {}'.format(nota))
elif nota <= 4.9:
    print('Aluno Reprovado {}'.format(nota))