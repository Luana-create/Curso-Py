# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
# Cuidado com a ordem de precedencia.

n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
media=(n1+n2)/2
print("A média do aluno é:{:.2f}".format(media))