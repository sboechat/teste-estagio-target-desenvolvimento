# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;


### JEITO FÁCIL

def tem_letra_a_jeito_facil(frase:str):
    return frase.lower().count('a')

def tem_letra_a_jeito_dificil(frase:str):
    cont = 0
    for letra in frase.lower():
        if letra == 'a':
            cont += 1
    return cont

def main():
    frase = input("Digite uma frase: ")
    print(tem_letra_a_jeito_facil(frase))
    print(tem_letra_a_jeito_dificil(frase))
    
if __name__ == "__main__":
    main()