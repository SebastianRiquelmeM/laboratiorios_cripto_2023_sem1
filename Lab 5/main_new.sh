#!/bin/bash
set -x  # Imprime cada comando antes de ejecutarlo

# Detiene todos los contenedores en ejecución
docker stop $(docker ps -aq)

# Elimina todos los contenedores
docker rm $(docker ps -aq)

# Elimina todas las imágenes
docker rmi $(docker images -q)

# Elimina todas las redes
docker network rm $(docker network ls -q)

# Navega al directorio s1 y construye la imagen
cd s1
docker build -t my_image_s1 .

cd ..

# Crea una red
docker network create mynetwork

# Ejecuta el contenedor s1 en segundo plano
docker run --network=mynetwork -d --name s1 my_image_s1

# Obtiene la dirección IP del contenedor s1
s1_ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' s1)

# Array de clientes
clients=("c1" "c2" "c3")

# Itera sobre cada cliente en el array
for client in ${clients[@]}; do
  # Navega al directorio del cliente y construye la imagen
  cd $client
  docker build -t my_custom_${client} .
  cd ..

  # Ejecuta el contenedor del cliente
  docker run --network=mynetwork -d -it --name $client my_custom_${client}

  # Espera 10 segundos
  sleep 10

  # Inicia tcpdump en el contenedor del cliente
  docker exec -d $client /bin/bash -c 'tcpdump -U -i any -w ./capture.pcap >/dev/null 2>&1 &'

  # Espera 10 segundos
  sleep 10

  # Realiza una conexión SSH al contenedor del cliente
  docker exec -it $client /bin/bash -c "sshpass -p 'test' ssh test@$s1_ip"

  # Espera unos segundos para asegurar que tcpdump termina de capturar
  sleep 10

  # Copia el archivo capture.pcap del contenedor del cliente al host
  timeout 10 docker cp ${client}:./capture.pcap ./captura_${client}.pcap
done

# Espera 10 segundos
sleep 10

# Inicia tcpdump en el contenedor s1
docker exec -d s1 /bin/bash -c 'tcpdump -U -i any -w ./capture.pcap >/dev/null 2>&1 &'

# Espera 10 segundos
sleep 10

# Realiza una conexión SSH al propio contenedor s1
docker exec -it s1 /bin/bash -c "sshpass -p 'test' ssh test@localhost"

# Espera unos segundos para asegurar que tcpdump termina de capturar
sleep 10

# Copia el archivo capture.pcap del contenedor s1 al host
timeout 10 docker cp s1:./capture.pcap ./captura_s1.pcap
