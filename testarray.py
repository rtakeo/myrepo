
palavra = "banana"
acertos = list("______")
conta_acertos = 0
letrasusadas = list("")
tentativas = 6
print("Tente acertar a palavra com " + str(len(palavra)) + " letras")
print(acertos)
while True:
    print("\n\n")
    print("tentativas restantes: " + str(tentativas))
    print("letras já utilizadas: " + str(letrasusadas))
    ok = False;
    while not ok:
        letra = input("letra: ")
        try:
            letrasusadas.index(letra)
            print("já usou essa letra")
        except ValueError:
            letrasusadas.append(letra)
            letrasusadas.sort()
            ok = True;
    i=0
    aux = conta_acertos
    for x in palavra:
        if letra == x:
            acertos[i]=letra
            print("acertou!!!")
            print(acertos)
            conta_acertos = conta_acertos + 1
        i=i+1
    if aux == conta_acertos:
        print("erroooooooouuuuu!!!!")
        tentativas=tentativas-1
    if conta_acertos == len(palavra):
        print("\n\n")
        print("vc venceu!!!")
        print(acertos)
        break
    if tentativas == 0:
        print("\n\n")
        print("vc perdeu!!!")
        print(acertos)
        break
    
