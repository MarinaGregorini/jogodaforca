
import random

# Função para escolher uma palavra aleatória
def escolher_palavra():
    palavras = ["panda", "urso", "elefante", "macaco"]
    palavra_aleatoria = random.choice(palavras)  # Escolhe uma palavra aleatória da lista
    letras_palavra = list(palavra_aleatoria)
    return letras_palavra  # Retorna as letras separadas da palavra escolhida
