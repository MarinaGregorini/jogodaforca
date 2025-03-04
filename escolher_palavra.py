import random

def escolher_palavra():
    palavras = ["panda", "urso", "elefante", "macaco"]
    palavra_aleatoria = random.choice(palavras)  
    letras_palavra = list(palavra_aleatoria)
    return letras_palavra
