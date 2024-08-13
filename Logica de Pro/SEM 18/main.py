import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'desenvolvedor', 'computador', 'jogo', 'desafio']
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas_max = 6
    tentativas = 0

    print("Bem-vindo ao jogo da forca!")
    print(mostrar_palavra(palavra, letras_corretas))
    
    while tentativas < tentativas_max:
        letra = input("Adivinhe uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, insira uma única letra.")
            continue

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            letras_corretas.add(letra)
            print(f"Boa! A letra '{letra}' está na palavra.")
        else:
            letras_erradas.add(letra)
            tentativas += 1
            print(f"Letra '{letra}' não está na palavra. Tentativas restantes: {tentativas_max - tentativas}")

        palavra_atual = mostrar_palavra(palavra, letras_corretas)
        print(palavra_atual)
        
        if '_' not in palavra_atual:
            print("Parabéns! Você adivinhou a palavra.")
            break
    else:
        print(f"Game over! A palavra era '{palavra}'.")

if __name__ == "__main__":
    jogo_da_forca()
