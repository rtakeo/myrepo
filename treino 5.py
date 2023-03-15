#For-loop using format()
#Autor: Rodrigo Takeo
#Motivo: Train different ways to do the same thing
#Data: 19/01/23

print("---The 5 Times Table---")
for row in range(1,6):
    for col in range(1,6):
        print("{:<5}".format(row*col), end="")
    print()