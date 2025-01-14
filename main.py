import random

letrasMin = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
letrasMai = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def criptografar():
    palavra = input("Digite uma mensagem para criptografar")
    chave = random.randint(1, 25)
    mensagemArray = []
    for i in palavra:
        if(i.islower() == True):
            index = letrasMin.index(i)
            index = (index+chave)% len(letrasMin)
            mensagemArray.append(letrasMin[index])
        elif(i == " "):
            mensagemArray.append(" ")
        else:
            index = letrasMai.index(i)
            index = (index+chave)% len(letrasMai)
            mensagemArray.append(letrasMai[index])
    resultado = "".join(str(i) for i in mensagemArray)
    print(f"Chave: {chave}")
    print(resultado)
    main()
    
def decriptografar():
    codigo = input("Digite ou copie a mensagem criptografada\n")
    chave = int(input("Digite a chave\n"))
    mensagemArray = [] 
    for i in codigo:
        if(i.islower() == True):
            index = int(letrasMin.index(i))-chave
            mensagemArray.append(letrasMin[index])
        elif(i == " "):
            mensagemArray.append(" ")
            continue
        else: 
            index = letrasMai.index(i)-chave
            mensagemArray.append(letrasMai[index])
    resultado = "".join(str(i) for i in mensagemArray)
    print(resultado)
    main()

def main():
    print("O que gostaria de fazer?")
    print("1 - Criptografar")
    print("2 - Decriptografar")
    escolha = input()
    while(True):
        try:
            direcao(escolha)
            break
        except ValueError:
            print("Digite somente 1 ou 2")
            escolha = input()

def direcao(escolha):
    if(escolha == "1"):
        criptografar()
    elif(escolha == "2"):
        decriptografar()
    else:
        raise ValueError

main()