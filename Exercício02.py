#Escreva um programa que receba o salário de um funcionário (float), e retorne o resultado do novo salário com reajuste de 35%. 

#Cores para dar uma enfeitada no terminal
from pprint import isrecursive
RED   = "\033[1;31m"  
RESET = "\033[0;0m"

print("Olá, bem vindo ao calculo de reajuste de salário!")
fSalary = float(input("Informe seu salário: "))

print("Seu salário sofreu um rajuste de 35'%' e saiu de: R$"+RED+"", str(fSalary), ""+RESET+" para R$"+RED+""+str((fSalary*0.35) + fSalary)+ ""+RESET+"!")
