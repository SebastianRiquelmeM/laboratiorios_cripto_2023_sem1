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
cd custom_ubuntu
docker build -t my_custom_ubuntu .

# Create a network
docker network create mynetwork

# Run the s1 container in the background
docker run --network=mynetwork -d --name s1 my_image_s1

docker run --network=mynetwork -it --name my_custom_ubuntu my_custom_ubuntu