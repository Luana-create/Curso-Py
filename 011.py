#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
larg=float(input('Qual a largura da parede em metros?' ))
alt=float(input("Qual a altura da parede em metros?" ))
area=larg*alt
litros=area/2
print('Sua parede tem as dimensões {:.2f} x {:.2f} e sua área é de {:.2f}m².\nSerá necessário {:.2f} litros de tinta para pintar os {:.2f}m²'.format(larg, alt,area, litros, area))
#Poderia ter optado por fazer dois print ao invés de usar \n, mas achei mais prático.