Jogo da Forca em Python

Este é um jogo da forca em Python, onde o objetivo é adivinhar uma palavra antes de cometer 6 erros.

Como Funciona

O jogo escolhe uma palavra aleatória de uma lista.
O jogador tenta adivinhar a palavra, uma letra por vez.
A cada erro, uma parte da forca é desenhada.
O jogador perde se errar 6 vezes ou ganha se adivinhar a palavra.

Explicação do Código

Funções
escolher_palavra(): Esta função escolhe uma palavra aleatória a partir de uma lista de palavras pré-definidas. A palavra é retornada para ser utilizada no jogo.

imprimir_palavra(letras_palavra): Exibe a palavra com as letras descobertas e as letras ainda ocultas (representadas por "_"). A função recebe a lista letras_palavra, que contém as letras corretas adivinhadas até o momento.

desenhar_forca(tentativas): Desenha a forca com base no número de tentativas erradas feitas pelo jogador. A cada erro, o desenho da forca é atualizado, com até 6 erros permitidos antes do jogador perder.

Variáveis

palavra_aleatoria: Armazena a palavra escolhida aleatoriamente pela função escolher_palavra(). Essa palavra é o objetivo que o jogador deve adivinhar.

letras_palavra: Uma lista que contém as letras da palavra secreta que foram descobertas pelo jogador. Inicialmente, todas as letras são representadas por "_". À medida que o jogador acerta as letras, as posições correspondentes são atualizadas.

tentativas: Um contador que armazena o número de tentativas erradas feitas pelo jogador. Se o número de tentativas erradas chegar a 6, o jogador perde.

letras_erradas: Uma lista que armazena as letras que o jogador tentou, mas não estão na palavra secreta.

Como Jogar

Execute o código com python main.py.
O jogo vai exibir uma palavra mascarada, e você deve digitar uma letra de cada vez.
Se acertar uma letra, ela será revelada. Se errar, a forca vai sendo desenhada.
O jogo termina quando você adivinhar a palavra ou cometer 6 erros.
