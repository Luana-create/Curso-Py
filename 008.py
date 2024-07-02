#Escreva um programa que leia um valor em metros e exiba convertido em centímetro e milimetros.
val-metros=float(input("Digite o valor que deseja converter: "))
val-cent= val-metros/100
val-mili= val-metros/1000
print("Este valor em centímetros é {:.2f} e em milímetros é {:.2f}".format(val-cent, val-mili))
