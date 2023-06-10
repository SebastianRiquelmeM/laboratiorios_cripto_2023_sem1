from scapy.all import *
import sys
import os

# Obtener el mensaje a cifrar desde los argumentos de la línea de comandos
mensaje = sys.argv[1]

# Generar valores aleatorios para el ID de paquete y el número de secuencia de ICMP
id_paquete = os.urandom(2)
num_secuencia = 1

# Enviar cada caracter del mensaje como un paquete ICMP de solicitud a la dirección IP de loopback
for caracter in mensaje:
    datos_aleatorios = os.urandom(44)
    datos = datos_aleatorios + b'\x00' * (47 - len(datos_aleatorios)) + bytes(caracter, 'utf-8') + b'\x00'
    #datos = datos_aleatorios + b'\x00' * (16 - len(datos_aleatorios)) + b'\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f' + bytes(caracter, 'utf-8') + b'\x00' + b'\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f' + b'\x30\x31\x32\x33\x34\x35\x36\x37' + b'\x00' * 8
    paquete = IP(dst="127.0.0.1", id=int.from_bytes(id_paquete, byteorder='big'))/ICMP(id=1, seq=num_secuencia)/Raw(load=datos)
    send(paquete)
    num_secuencia += 1

  