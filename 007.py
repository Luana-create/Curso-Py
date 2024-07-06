# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
# Cuidado com a ordem de precedencia.

n1=float(input("Primeira nota do aluno: "))
n2=float(input("Segunda nota do aluno: "))

media=(n1+n2)/2

print("A média do aluno é:{:.2f}".format(media))