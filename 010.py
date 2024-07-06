#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
real=float(input('Quanto dinheiro você tem na carteira?R$'))
dolar= real/3.27#Hoje tá 5,46 em julho de 2024
print("Com R${:.2f} você pode comprar até US${:.2f} dolares com este valor".format(real, dolar))
#OBS sempre esqueço na hora de formatar o 2f de colocar o .
#Se esquecer vai bugar completamente o codigo.
#Tem que ser :.2f
