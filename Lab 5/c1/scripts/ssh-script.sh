#!/bin/bash
# ssh-script.sh

# Start tcpdump capturing packets and send it to the background
tcpdump -i any -w /captures/capture.pcap 'port 22 and host s1' &

# Attempt SSH connection
sshpass -p 'test' ssh -o StrictHostKeyChecking=no test@s1
