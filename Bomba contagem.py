#Bomba contagem
#Autor: Rodrigo Takeo
#Motivo: Desafio do meu pai
#Data:19/01/23
import time

count = 10
answer = input("You are in danger! Would you like to continue? \nEnter (y)es or (n)o:   ")
answer = answer.upper()
if answer == 'y'.upper() or answer == 'yes'.upper():
    while not count == 0:
        print(count, end="\n ")
        count -= 1
        time.sleep(1)
if count == 0:
    print("BOOM!!")