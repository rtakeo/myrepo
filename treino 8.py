import time
def getInt(prompt):
    ''' Get's an Integer from Keyboard Input.
    '''
    while True:
        data = input(prompt)
        if len( data ) > 0:     # check empty string
            post = data
            if data[0] == '-':
                post = data[1:]  # return substring without negative
            if post.isnumeric(): # checks numbers are left in the string
                return int(data)
def cToF(celsius):
    ''' Convert temp between celsius and farenheight.
    '''
    farenheight = 0
    farenheight = celsius * 9/5 + 32
    return farenheight

# ..main.. Input Processing and Output
print("Welcome to Celsius to Farenheight Converter")
while True:    
    temp = input("Please enter celsius (Q)uit: ")
    if temp.lower() == 'q' or temp.lower() == 'quit': 
        print("See you next time")
        time.sleep(1)
        exit()
    else:
        temp = int(temp)
        print("Temp in Farenheight is", cToF(temp))
        time.sleep(0.5)
            