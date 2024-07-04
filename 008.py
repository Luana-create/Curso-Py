#Escreva um programa que leia um valor em metros e exiba convertido em centímetro e milimetros.
valMetros=float(input("Digite o valor que deseja converter: "))
valCent= valMetros*100
valMili= valMetros*1000
print("Este valor em centímetros é {:.2f} e em milímetros é {:.2f}".format(valCent, valMili))
