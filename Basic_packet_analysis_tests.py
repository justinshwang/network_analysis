from Basic_packet_analysis import *
import pyshark

##IDEAS##

# 1. Look for what IP went to an IP of interest --> Who followed a link, uploaded some data, etc.
# 2. Look for a file that was downloaded --> Looking for malicious files to see if machine got infected
# 3. Look for when (time) a file was downloaded --> To see if data exfiltration or strange behavior started soon after
# 4. Look for the dst IP and port used --> To review the data going out the door
# 5. What protocol is being used?  Are we dealing with TCP, UDP, ICMP?  It will help focus where to start based on why you went looking in the first place.  What made you suspect the traffic and what protocol would it use.
# 6. Look at the source port -->  Is it staying constant or is it changing?  A source port should stay constant for each session, but change (usually incremental) for the next session.  A constant source port can indicate a poor coding (or deliberate) in a tool or malware.  It is a characteristic that might eventually help you ID what tool/malware it might be.
# 7. Look at the sequence numbers -->  Are they changing like they should or are they staying constant.  It can indicate many things depending on the scenario.
# 8. I look at the TTLs (same IP but widely varying; etc), IPID/fragID (fixed or changing), flag fields (IP and TCP headers), etc.  Any of the packet fields to see if the traffic is behaving normally.  (if its a large capture, this is much more difficult and time consuming)
# 9. If you use wireshark to do your packet analysis, it has some great features to give you statistics about your packet capture.  This can help you find interesting pieces of traffic to start your analysis.

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

