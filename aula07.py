#OPERAÇÕES:
# adiçao +
#subtração -
#multiplicação * 
#divisão /
#exponenciação **
#Divisão inteira //
#Resto da divisao % 
#5+2==7
#5-2==3
#5*2==10
#5/2==2.5
#5**2==25
#5//2==2
#5%2==1
#Ordem de Precedência
#1º ()
#2° **
#3º* / // %
#4º + - 

#nome=input('Qual seu nome?')
#print("Prazer em te conhecer {:=^20}!".format(nome))

n1= int(input('Um valor: '))
n2=int(input('Outro valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
ex=n1**n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d), end='')
print('A divisão inteira é {}\n e a potencia {}'.format(di,ex))

#end='' mantem na mesma linha
#\n quebra a linha no meio do print
#end=>>> é colocado após manter na mesma linha