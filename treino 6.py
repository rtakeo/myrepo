# for-loop with 'in'
#Autor: Rodrigo Takeo
#Motivo: Treino
#Data: 23/01/23

data = "The Quick brown Fox Jumped over the lazy cat"
spaces = 0
for x in data:
    if x == ' ':
        spaces += 1
print("Number of spaces in data is", spaces)