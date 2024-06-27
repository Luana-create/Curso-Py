n = float(input('Digite um valor: '))
n1 = str(input('Digite um valor: '))
n2 = bool(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))


print(type[n])

print(n1.isnumeric())
# isnumeric: é possivel converter este numero em um tipo primitivo int?
print(n1.isalpha())  # isalpha: é alfabetico? é letra?
print(n1.isalnum())  # isalnum: é alfanumerico?é letra ou numero.
