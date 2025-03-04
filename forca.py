from desenharforca import desenhar_forca

def escolher_letra():
    input_letra =(input("Tenta uma letra: ")).lower()
    return input_letra

tentativa = 0
def verificar_letra(letras_palavra, input_letra):
    global tentativa
    if input_letra in letras_palavra:
        return input_letra
    else:
        tentativa += 1
        print(f"A letra {input_letra} não faz parte desta palavra.")
        desenhar_forca(tentativa)
        print(tentativa)
        return tentativa