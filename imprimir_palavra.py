def imprimir_palavra(letras_palavra, input_letra=None):
    global impressao_passada
    if input_letra == None:
        if impressao_passada == None:
            for letra in letras_palavra:
                print("_", end=" ")
        else:
            for letra in impressao_passada:
                print(letra, end=" ")
    else:
        for letra in letras_palavra:
            if letra == input_letra:
                impressao_passada.append(letra)
                print(letra, end=" ")
            elif letra != input_letra:
                impressao_passada.append("_")
                print("_", end=" ")
        print(impressao_passada)
                
