# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = float(input("Digite um número:"))
d = n*2
t = n*3
r = n**(1/2)

print("O dobro de {:.2f} é {:.2f},\no triplo é {:.2f} \ne sua raiz quadrada é {:.2f}".format(
    n, d, t, r))

print("O dobro de {:.2f} é {:.2f},\no triplo é {:.2f} \ne sua raiz quadrada é {:.2f}".format(
    n, (n*2), (n*3), (n**(1/2))))

# outra forma de fazer raiz quadrada é usando a função pow

print("O dobro de {:.2f} é {:.2f},\no triplo é {:.2f} \ne sua raiz quadrada é {:.2f}".format(
    n, (n*2), (n*3), pow(n, (1/2))))
