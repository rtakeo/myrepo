import requests, random

the_web_page_as_a_string = requests.get("https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt").content
aux = str(the_web_page_as_a_string[0:len(the_web_page_as_a_string)])
palavras = aux.split("\\n")
s = random.randint(1,len(palavras))

palavra = palavras[s]
acertos = list()
for x in palavra:
    acertos.append("_")
    
conta_acertos = 0
letrasusadas = list("")
tentativas = len(palavra)
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
    
    if conta_acertos <= aux:
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
        print("a palavra era " + palavra)
        break
print(" End ")
    
