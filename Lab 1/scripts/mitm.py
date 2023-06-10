from scapy.all import *

# Función para cifrar el string usando César
def cifrar_cesar(texto, clave):
    cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            mayuscula = caracter.isupper()
            caracter = caracter.lower()
            ascii_code = ord(caracter)
            codigo_cifrado = (ascii_code + clave - 97) % 26 + 97
            cifrado += chr(codigo_cifrado).upper() if mayuscula else chr(codigo_cifrado)
        else:
            cifrado += caracter
    return cifrado

# Abre el archivo de captura
packets = rdpcap("captura_ping_script.pcapng")

# Inicializa el string vacío
caracteres_concatenados = ""

# Itera sobre los paquetes y busca los paquetes ICMP con dirección de destino 127.0.0.1
for packet in packets:
    if ICMP in packet and packet[IP].dst == "127.0.0.1":
        # Obtiene el contenido del campo data
        data = packet[ICMP].load
        # Accede al caracter en la posición 45 del contenido
        caracter_45 = chr(data[44])
        # Omite el primer paquete que contiene una "i"
        if caracter_45 == "i" and caracteres_concatenados == "":
            continue
        # Concatena el caracter al string
        caracteres_concatenados += caracter_45

# Imprime el string original
print(f"String original: {caracteres_concatenados}")


# Inicializa la lista vacía
cifrados = []

# Imprime todas las combinaciones del cifrado César
for clave in range(26):
    # Cifra el string usando la clave actual de César
    cifrado = cifrar_cesar(caracteres_concatenados, clave)
    # Agrega el cifrado a la lista de cifrados
    cifrados.append(cifrado)

# Diccionario
import os
from unidecode import unidecode

def leer_diccionario():
    # Crea una lista vacía para almacenar las palabras
    palabras = []
    # Obtiene la lista de archivos en la carpeta ./dics
    archivos = os.listdir("./dics")
    # Itera sobre cada archivo en la lista de archivos
    for archivo in archivos:
        # Abre el archivo de texto en modo lectura
        with open(f"./dics/{archivo}", "r") as f:
            # Itera sobre cada línea del archivo de texto
            for linea in f:
                # Elimina los caracteres de nueva línea de la línea
                linea = linea.strip()
                # Agrega la línea a la lista de palabras
                palabras.append(linea)
                # Si la línea tiene tildes, agrega también la línea sin tildes
                if any(c in "áéíóúüÁÉÍÓÚÜ" for c in linea):
                    palabras.append(unidecode(linea))
    # Devuelve la lista de palabras completa
    return palabras

def encontrar_posicion_mas_coincidencias(lista_caracteres, lista_palabras):
    max_coincidencias = 0
    posicion_mas_coincidencias = 0
    for i, caracteres in enumerate(lista_caracteres):
        coincidencias = 0
        for palabra in lista_palabras:
            if palabra in caracteres:
                coincidencias += 1
        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            posicion_mas_coincidencias = i
    return posicion_mas_coincidencias


""" print(encontrar_posicion_mas_coincidencias(cifrados, leer_diccionario()))
print("\n")
print(cifrados[encontrar_posicion_mas_coincidencias(cifrados, leer_diccionario())])
print("\n")
print(cifrados)
 """

# Encuentra la posición del cifrado con más coincidencias en el diccionario
posicion_max_coincidencias = encontrar_posicion_mas_coincidencias(cifrados, leer_diccionario())

# Imprime todos los cifrados, resaltando en verde el que tiene más coincidencias
for i, cifrado in enumerate(cifrados):
    if i == posicion_max_coincidencias:
        print('\033[92m' + cifrado + '\033[0m')
    else:
        print(cifrado)
