#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

#Cores para dar uma enfeitada no terminal
from pprint import isrecursive
RED   = "\033[1;31m"  
RESET = "\033[0;0m"

i = 0
fResult = 0

print("Bem vindo ao calculo de média!")

for x in range(4):
    i += 1
    fAverage = float(input("Informe a nota "+ str(i)+": "))  
    fResult += fAverage

print("A sua média é:"+RED+"", fResult/4,""+RESET)
   