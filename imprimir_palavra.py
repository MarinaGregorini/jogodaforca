def imprimir_palavra(letras_palavra, input_letra=None):
    impressao_passada = []
    if input_letra == None:
        if not impressao_passada:
            for letra in letras_palavra:
                print("_", end=" ")
        else:
            for letra in impressao_passada:
                print(letra, end=" ")
    else:
        for letra in letras_palavra:
            if letra == input_letra:
                print(letra, end=" ")
            else:
                print("_", end=" ")
                
