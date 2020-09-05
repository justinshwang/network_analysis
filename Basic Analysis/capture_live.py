import pyshark

class Sniffer():
    pkt_num = 0
    out_string = ""

    cap = pyshark.LiveCapture(interface='en0')

    cap.sniff(packet_count=5)

    for pkt in cap:
        out_file = open("livecapture.txt", "w")
        out_string += "Packet #" + str(pkt_num)
        out_string += "\n"
        out_string += str(pkt)
        out_string += "\n"
        out_file.write(out_string)
        i = i + 1
    cap.close()