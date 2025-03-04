def imprimir_palavra(letras_palavra, impressao_passada, input_letra=None):
    if input_letra is not None:
        for i, letra in enumerate(letras_palavra):
            if letra == input_letra:
                impressao_passada[i] = letra 

    print(" ".join(impressao_passada)) 