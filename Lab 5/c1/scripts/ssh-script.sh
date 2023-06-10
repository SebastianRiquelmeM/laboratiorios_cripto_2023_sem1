#!/bin/bash
# ssh-script.sh

# The first argument is the IP address of the s1 container
s1_ip=$1

echo "Starting tcpdump..."

# Start tcpdump capturing packets and send it to the background
tcpdump -i any -w /captures/capture.pcap &

# Get the PID of tcpdump
PID=$!

echo "Tcpdump started with PID $PID."

# Attempt SSH connection
echo "Attempting SSH connection..."
sshpass -p 'test' ssh -o StrictHostKeyChecking=no test@$s1_ip

echo "SSH connection attempted."

# Kill tcpdump process and wait for it to finish writing the pcap file
echo "Killing tcpdump..."
kill $PID
wait $PID

echo "Tcpdump killed. Exiting script."
