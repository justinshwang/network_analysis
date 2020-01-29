from Basic_packet_analysis import *
import pyshark

##Basic Packet Analysis Testing - Organize packet data and output

## 1. File of captured packetss

pkts = pyshark.FileCapture('capturetest1.cap')

print("Ready to print source and destination addresses and ports...")
input()

pkts.apply_on_packets(print_conversation_header, timeout=100)

#adding only_summaries returns basic summary info of packets, but faster 
#pkts = pyshark.FileCapture('capturetest2.cap', only_summaries = True)

#Can also add display_filter = "dns" // etc.

print("Ready to print DNS query and response names...")
input()

pkts.apply_on_packets(print_dns_info, timeout=100)


## 2. Live capture of packet data

# Live capture of packets only using bpf filter

# pkts = pyshark.LiveCapture(interface='en0', bpf_filter = 'ip and tcp port 80')
# pkts.sniff(timeout=5)
# print(pkts)


## 3. Misc. Information

print("Getting packet count and highest layers...")
input()
print("Packet total:" + str(get_capture_count(pkts)))
print("Packet total:" + str(get_highest_layers(pkts)))

# Press any key to view further packet information
print("Ready to print all packet information...")
input()

for pkt in pkts:
    print(pkt)

