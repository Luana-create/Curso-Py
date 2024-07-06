#Faça um algoritmo que mostra o preço de um produto e mostre seu novo preço, com desconto de 5% de desconto.
x=float(input("Valor original do produto:"))
d= (x*0.05)
vd= x-d
print("O produto que custava {}, com desconto de 5% para a custar {}".format(x, vd))

