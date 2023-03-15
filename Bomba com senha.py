#Bomba com senha
#Autor: Rodrigo Takeo
#Motivo: Desafio próprio
#Data: 19/01/23


chances = 3
print("Tip... \nThe password is the date of the older brother's birthdate")
password = ""
while not password == '1802' and chances > 0:
    password = input("Please enter the password: ")
    if not password.isnumeric():
        print("Password is numeric!!!")
        continue
    chances -= 1
    if chances > 0:
        print("Mistakes left " + str(chances))
        print("Please try again.....")
if password.isnumeric() and int(password) == 1802:
    print("Congratulations!!!")
else:
    print("\n BOOM!!!")
    
    
    