#1.	Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule e imprima o valor de z:

#Cores para dar uma enfeitada no terminal
from pprint import isrecursive
RED   = "\033[1;31m"  
RESET = "\033[0;0m"

iFirstNumber = 0
iSecondNumber = 0

#Realiza a requição dos valores
def defRequestNumber():
    #Recebendo valores de uma var Global
    global iFirstNumber
    global iSecondNumber
    
    #Recebe primeiro valor
    iFirstNumber = int(input("Informe o valor de "+RED+"X"+RESET+": "))
    iSecondNumber = int(input("Informe o valor de "+RED+"Y"+RESET+": "))

    #Imprime o resultado dos valores requisitados
    print ("Você escolheu X igual a: "+str(iFirstNumber)+"\ne escolheu Y igual a: " + str(iSecondNumber))
defRequestNumber()

def defDecision():
    #Caso o usuário queira trocar os valores ja informado
    sDecision = str(input ("\nPara alterar os valor informe a letra S, para manter os valores informe a letra N: ").upper()) 

    #Só faz algo se receber "S" (Minusculo ou Maiúsculo)
    if sDecision == "S":    
        defRequestNumber()
    
    else:
        exit
defDecision()
            
#Somente para auxiliar no Layout
input("\nPrecione "+RED+"ENTER"+RESET+" para continuar...")

def defOperation():
    iResult = ((iFirstNumber * iFirstNumber) + (iSecondNumber * iSecondNumber)) / (iFirstNumber - iSecondNumber)
    print("Z é igual a: "+str(iResult))
defOperation()



