print("Termo")
print("=====")

palavra = input("Digite uma palavra: ")
aux = ""
for i in range(len(palavra)):
    aux = aux + "_ ,"
print(aux[0:len(aux)-1])
while True: 
    entrada = input("Tente acertar a palavra, digite uma palavra de " + len(palavra) + " : ")
    for c in palavra:
        
        





