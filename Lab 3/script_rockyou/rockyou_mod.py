# Importamos el módulo necesario
import re

# Nombre de los archivos de entrada y salida
input_file = "rockyou.txt"
output_file = "rockyou_mod.dic"

# Contador para las contraseñas modificadas
count = 0

# Abrimos los archivos de entrada y salida
with open(input_file, "r", encoding="latin-1") as infile, open(output_file, "w", encoding="latin-1") as outfile:
    for line in infile:
        # Eliminamos los espacios en blanco al principio y al final
        line = line.strip()
        # Verificamos si la línea comienza con una letra
        if re.match(r'^[a-zA-Z]', line):
            # Modificamos la primera letra y agregamos un cero al final
            line = line[0].upper() + line[1:] + '0'
            # Escribimos la línea en el archivo de salida
            outfile.write(line + '\n')
            # Incrementamos el contador
            count += 1

# Imprimimos el número de contraseñas en el diccionario modificado
print(f"El diccionario modificado contiene {count} contraseñas.")
