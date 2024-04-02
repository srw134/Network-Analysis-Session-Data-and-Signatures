from scapy.all import *

packet = IP(dst="172.31.130.10")/TCP(dport=80, flags='S', window=4128)
send(packet)