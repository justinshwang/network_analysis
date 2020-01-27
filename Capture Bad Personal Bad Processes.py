import pyshark


pkt_arr = []

# Testing - Capture number of packets

def counter(*args):
    pkt = args[0]
    pkt_arr.append(pkt)
    input()
    print(pkt[pkt.highest_layer].pkt_app.request_uri)

def get_capture_count(pkts):

    pkts.apply_on_packets(counter, timeout = 10000)
    return len(pkt_arr)

# Print highest layers

def highest_layers(*args):
    pkt = args[0]
    input()
    print(pkt[pkt.highest_layer])

def get_highest_layers(pkts):
    pkts.apply_on_packets(highest_layers, timeout = 10000)
    return 1


##Testing 

# File of captured packetss

pkts = pyshark.FileCapture('capturetest2.cap')

# Function Calls

print("Packet total:" + str(get_capture_count(pkts)))
print("Highest_layers: " + str(get_highest_layers(pkts)))


# Press any key to view further packet information
input()

for pkt in pkts:
    print(pkt)

