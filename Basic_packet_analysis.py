import pyshark


pkt_arr = []

# Capture number of packets

def counter(*args):
    pkt = args[0]
    pkt_arr.append(pkt)
    # print(pkt[pkt.highest_layer].pkt_app.request_uri)

def get_capture_count(pkts):
    pkts.apply_on_packets(counter, timeout = 10000)
    return len(pkt_arr)


# Print highest layers

def highest_layers(*args):
    pkt = args[0]
    # print(pkt[pkt.highest_layer])

def get_highest_layers(pkts):
    pkts.apply_on_packets(highest_layers, timeout = 10000)
    return 1


# DNS display basic info

def print_dns_info(pkt):
    try:
        if (pkt.dns.qry_name):
            print('DNS Request from %s: %s', pkt.ip.src, pkt.dns.qry_name)
        elif (pkt.dns.resp_name):
            print('DNS Response from %s: %s', pkt.ip.src, pkt.dns.resp_name)
    except AttributeError as e:
        print("No DNS info")
    
        
# Source and Destination addresses and ports display
        
def print_conversation_header(pkt):
    try:
        protocol =  pkt.transport_layer
        src_addr = pkt.ip.src
        src_port = pkt[pkt.transport_layer].srcport
        dst_addr = pkt.ip.dst
        dst_port = pkt[pkt.transport_layer].dstport
        print(protocol, src_addr, src_port, dst_addr, dst_port)
    except AttributeError as e:
        #ignore packets that aren't TCP/UDP or IPv4
        pass