from scapy.all import *

packet = IP(dst="target-ip")/TCP(dport=80, flags='S', window=4128)
send(packet)