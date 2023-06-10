import sys

def cifrado_cesar(texto, corrimiento):
    cifrado = ''
    for letra in texto:
        # Si la letra es una letra mayúscula
        if letra.isupper():
            cifrado += chr((ord(letra) + corrimiento - 65) % 26 + 65)
        # Si la letra es una letra minúscula
        elif letra.islower():
            cifrado += chr((ord(letra) + corrimiento - 97) % 26 + 97)
        # Si el caracter no es una letra (como un espacio en blanco o un signo de puntuación), se mantiene igual
        else:
            cifrado += letra

    return cifrado


# Si no se ingresan los argumentos adecuados, se muestra un mensaje de ayuda
if len(sys.argv) != 3:
    print('Uso: python cifrado_cesar.py "texto a cifrar" corrimiento')
else:
    texto = sys.argv[1]
    corrimiento = int(sys.argv[2])
    texto_cifrado = cifrado_cesar(texto, corrimiento)
    print(texto_cifrado)

