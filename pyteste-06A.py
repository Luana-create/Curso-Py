#Soma já definindo tipos primitivos não causa concatenação
n1=int(input('digite um valor:'))
n2=int(input('digite um valor:'))
s= n1 + n2
#print('A soma vale:', s)
#usando mascaras do format
print ('A soma entre {} e {} vale {}'.format(n1, n2, s))
