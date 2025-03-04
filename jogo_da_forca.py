from imprimir_palavra import imprimir_palavra
from verificar_palavra import escolher_letra, verificar_letra
from escolher_palavra import escolher_palavra
from desenhar_forca import desenhar_forca

print("Jogo da forca.")

letras_palavra = escolher_palavra()

impressao_passada = ["_"] * len(letras_palavra)
print(" ".join("_" for _ in impressao_passada))

tentativa = 0
while tentativa < 6 and "_" in impressao_passada:
    
    input_letra = escolher_letra()
    
    acertou = verificar_letra(letras_palavra, input_letra)
    if acertou == False:
        tentativa += 1
        desenhar_forca(tentativa)
        
    imprimir_palavra(letras_palavra, impressao_passada, input_letra)
    
if "_" not in impressao_passada:
    print("Parabéns!")

elif tentativa >= 6:
    print("RIP") 
    print("A palavra era", "".join(letras_palavra)) 
    
    
    