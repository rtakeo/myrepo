#Treino if-blocks
#Autor: Rodrigo Takeo
#Motivo: Treinar o funcionamento de vários If-blocks conectados
#Data: 18/01/23

from pcinput import getInteger

print("Hello, can you give me some numbers please?")

a = getInteger("Please enter a number for 'a':")
b = getInteger("Please enter a number for 'b':")
c = getInteger("Please enter a number for 'c':")
d = 0
if a < d or b < d or c < d: 
    print("Oh!!! So you got some negative numbers to me? No problem... ")
if a > b:
    if b > c:
        print("{},{},{}".format(a,b,c))
    else:
        if a > c:
            print("{},{},{}".format(a,c,b))
        else:
            print("{},{},{}".format(c,a,b))
elif a > c:
    print("{},{},{}".format(b,a,c))
else:
    if b > c:
        print("{},{},{}".format(b,c,a))
    else:
        print("{},{},{}".format(c,b,a))
print("...All Sorted...")

