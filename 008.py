# Escreva um programa que leia um valor em metros e exiba convertido em centímetro e milimetros.
# km hm dam m dm mm
medida = float(input("Digite o valor que deseja converter: "))
valCent = medida*100  # centimetros
valMili = medida*1000  # milimetros
# valKm=medida/100
print("Esta medida em centímetros é {:.0f}cm \ne em milímetros é {:.0f}mm".format(
    valCent, valMili))
print('Caso queira saber este valor em ')
