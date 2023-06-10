# Dockerfile
FROM ubuntu:18.10
RUN apt-get update && apt-get install -y openssh-client sshpass
ADD ../scripts/ssh-script.sh /ssh-script.sh
RUN chmod +x /ssh-script.sh
CMD ["/ssh-script.sh"]
