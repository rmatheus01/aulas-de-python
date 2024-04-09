import os


nome = str (input ("Digite seu nome:"))
n1 = int (input ("Digite o seu primeiro numero:"))
n2 = int (input ("Digite o seu segundo numero:"))
maiorNum = 0
menorNum = 99999

#FAZENDO AS OPERAÇÃOES
soma = n1 + n2
produto = n1 * n2
media = soma / 2

if maiorNum < n1:
    maiorNum = n1

if menorNum < n2:
    menorNum = n1

if maiorNum > n1:
    menorNum =n2

print (media)
print (produto)
print (f"O seu primeiro numero: {n1}")
print (f"O seu segundo numero: {n2}")
