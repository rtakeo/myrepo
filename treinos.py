#Continuação de condição
#Autor: Rodrigo Takeo
#Motivo: Treinar mais a os blocos de condiçao (if-blocks)
#Data: 18/01/23

from pcinput import getInteger
temp =getInteger("please enter a temperature in celsius: ")

if temp > 70:
    print("Maybe this num is higher than the possible real temp, try a lower one")
elif temp > 50:
    print("It's very hot outside")
elif temp > 35:
    print("It's hot outside")
elif temp > 20:
    print("It's cool outside")
elif temp < -10:
    print("Maybe this num is lower than the possible real temp, try a higher one")
else:
    print("It's cold outside")
print("...End Program...")