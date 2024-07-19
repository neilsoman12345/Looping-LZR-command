import subprocess
import time

# List of port numbers to loop through
port_numbers = [80,443,7547,22,30005,5060,21,25,2000,8080,50805,4567,53,49154,49152,8081,8089,110,3306,8085,8000,143,51005,3389,587,58000,993,995,465,23,8443,1723,179,5432,1883,5672,8883,1521,53194,62220,6379,5900,20000,161,65535,1433,445,631,6443,623,47808,27017,502,102,11211]  

# Source IP address
source_ip = "172.29.64.1"

# Interface to use
interface = "eth0"

# Target IP range
target_range = "179.118.223.0/16"

# Command template
LZR_command_template = (
    "sudo zmap --target-port={port} --output-filter='success = 1 && repeat = 0' \
    -f 'saddr,daddr,sport,dport,seqnum,acknum,window' -O json --source-ip={source_ip} -o port{port}_result.json {target_range} | \
    sudo ./lzr --handshakes http,tls --sendInterface {interface}"
  )

# Function to run the command
def run_command(port_number):
    command = LZR_command_template.format(
        port=port_number,
        source_ip=source_ip,
        target_range=target_range,
        interface=interface
)
    print(f"Running command for port {port_number}...")
    subprocess.run(command, shell=True)

# Loop through port numbers and run the command
for port in port_numbers:
    run_command(port)
