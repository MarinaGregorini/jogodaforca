from desenharforca import desenhar_forca

def escolher_letra():
    input_letra =(input("Tenta uma letra: ")).lower()
    return input_letra


def verificar_letra(letras_palavra, input_letra):
    if input_letra in letras_palavra:
        return input_letra
    else:
        tentativa += 1
        desenhar_forca(tentativa)