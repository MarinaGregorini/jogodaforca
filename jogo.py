from imprimir_palavra import imprimir_palavra
from forca import escolher_letra, veriificar_letra
from listadepalavras import escolher_palavra

tentativa = 0
while tentativa < 6:
    escolher_letra()
    
    escolher_palavra()
    imprimir_palavra(letras_palavra, input_letra)
    
    