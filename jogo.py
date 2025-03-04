from imprimir_palavra import imprimir_palavra
from forca import escolher_letra, verificar_letra, tentativa
from listadepalavras import escolher_palavra

print("Jogo da forca.")

letras_palavra = escolher_palavra()

impressao_passada = ["_"] * len(letras_palavra)
print(" ".join("_" for _ in impressao_passada))

while tentativa < 6 and "_" in impressao_passada:
    
    input_letra = escolher_letra()
    
    verificar_letra(letras_palavra, input_letra)
    
    imprimir_palavra(letras_palavra, impressao_passada, input_letra)
    
if "_" not in impressao_passada:
    print("Parabéns!")

elif tentativa >= 6:
    print("RIP") 
    
    
    
    