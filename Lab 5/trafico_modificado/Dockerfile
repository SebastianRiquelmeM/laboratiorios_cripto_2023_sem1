# Dockerfile
FROM ubuntu:20.10

RUN sed -i -re 's/([a-z]{2}\.)?archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y build-essential zlib1g-dev libssl-dev libpam0g-dev unzip autoconf automake

RUN apt-get install -y wget git sshpass
RUN wget https://github.com/openssh/openssh-portable/archive/V_8_3_P1.zip
RUN unzip V_8_3_P1.zip && cd openssh-portable-V_8_3_P1 && \
    sed -i 's/#define SSH_VERSION.*/#define SSH_VERSION "SSH-2.0-OpenSSH_?"/' version.h && \
    autoreconf -fi && ./configure && make && make install

RUN useradd -m test && echo 'test:test' | chpasswd
RUN mkdir /var/run/sshd
EXPOSE 22
CMD ["/usr/local/sbin/sshd", "-D"]
