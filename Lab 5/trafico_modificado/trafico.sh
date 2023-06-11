#!/bin/bash
set -x  # Imprime cada comando antes de ejecutarlo

# Crea el directorio "capturas" si no existe
mkdir -p capturas

# Detiene todos los contenedores en ejecución
docker stop $(docker ps -aq)

# Elimina todos los contenedores
docker rm $(docker ps -aq)

# Elimina todas las imágenes
docker rmi $(docker images -q)

# Elimina todas las redes
docker network rm $(docker network ls -q)

# Construye la imagen Docker
docker build -t my_image_s1 .

# Crea una red
docker network create mynetwork

# Ejecuta el contenedor s1 en segundo plano
docker run --network=mynetwork -d --name s1 my_image_s1

# Obtiene la dirección IP del contenedor s1
s1_ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' s1)

# Inicia tcpdump en el contenedor s1
docker exec -d s1 /bin/bash -c 'tcpdump -U -i any -w /tmp/capture.pcap >/dev/null 2>&1 &'

# Espera 10 segundos
sleep 10

# Realiza una conexión SSH al propio contenedor s1
docker exec -it s1 /bin/bash -c "sshpass -p 'test' ssh -o StrictHostKeyChecking=no test@localhost"

# Espera unos segundos para asegurar que tcpdump termina de capturar
sleep 10

# Copia el archivo capture.pcap del contenedor s1 al directorio capturas en el host
docker cp s1:/tmp/capture.pcap ./capturas/captura_s1.pcap
