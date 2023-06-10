#!/bin/bash
set -x

# Stop all running containers
docker stop $(docker ps -aq)

# Remove all containers
docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q)

# Remove all networks
docker network rm $(docker network ls -q)

# Navigate to the s1 directory and build the image
cd s1
docker build -t my_image_s1 .

cd ..

# Navigate to the c1 directory and build the image
cd c1
docker build -t my_custom_image_c1 .

# Create a network
docker network create mynetwork

# Run the s1 container in the background
docker run --network=mynetwork -d --name s1 my_image_s1

# Wait for a while to allow the s1 container to fully start
sleep 10

# Get the IP address of the s1 container
s1_ip=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' s1)

# Run the c1 container in the background with elevated privileges, pass s1_ip as an argument to ssh-script.sh, wait for 20 seconds, then stop it
timeout 60 docker run --network=mynetwork --privileged -v "$(pwd)/captures:/captures" --name c1 my_custom_image_c1 /ssh-script.sh $s1_ip

# The script ends here
