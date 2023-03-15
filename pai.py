from pcinput import getInteger
array = []
while True:
        try:
            aux = input("num: ")
            if aux != "":
                i = int ( aux )
            else:
                break
        except ValueError:
            print( "That is not an integer -- please try again" )
            continue
        array.append(i)
array.sort()
print(array)
    
    
