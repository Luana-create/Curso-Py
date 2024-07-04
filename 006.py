#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n=int(float(input("Digite um número:")))
n1=n*2
n2=n*3
n3=n**(1/2)
print("O dobro do número é {:.2f}, o triplo é {:.2f} e sua raiz quadrada é {:.2f}".format(n1, n2, n3))