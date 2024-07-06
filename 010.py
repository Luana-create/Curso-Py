#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
din=float(input('Quanto dinheiro você tem na carteira?R$'))
conv= din/3.27#Hoje tá 5,46 em julho de 2024
print("Com {} pode comprar até {:2} dolares com este valor".format(din, conv))
