def imprimir_palavra(letras_palavra, input_letra=None):
    if input_letra == None:
        for letra in letras_palavra:
            print("_", end=" ")
    else:
        for letra in letras_palavra:
            if letra == input_letra:
                print(letra, end=" ")
            else:
                print("_", end=" ")
                
