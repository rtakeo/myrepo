from pcinput import getInteger

def cToF(data):
    fahrenheit = 0
    celsius = int(data)
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
while True:
    number = getInteger("Enter Celsius: ")
    print ("Temp in Fahrenheit", cToF(number))
