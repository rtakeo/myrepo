# For-loop inside a for-loop
#Autor: Rodrigo Takeo
#Motivo: Understand different types of for-loops
#Data: 19/01/23

print("---------The 5 Times Table--------")
for row in range(1,6):
    for col in range(1,6):
        print(row * col, end="\t")
    print()