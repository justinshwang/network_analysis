from packet import *

file = "capture1.pcap"

p = Packet(file)
p.print_IP_info(0)
