# Dockerfile
FROM ubuntu:14.10
RUN sed -i -re 's/([a-z]{2}\.)?archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y openssh-client sshpass tcpdump
CMD ["bash"]
