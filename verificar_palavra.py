def escolher_letra():
    while True:
        input_letra =(input("Tenta uma letra: ")).lower()
        if input_letra.isalpha() and len(input_letra) == 1:
            return input_letra
        else:
            print("Entrada inválida.")
            continue

def verificar_letra(letras_palavra, input_letra):
    if input_letra in letras_palavra:
        return True
    else:
        print(f"A letra {input_letra} não faz parte desta palavra.")
        return False
