import pyshark

class Packet(object):

    def __init__(self, file):
        self.cap = pyshark.FileCapture(file)
        self.num_pkts = len(self.cap)
        self.file = file

    def print_dns(self):
        cap = pyshark.FileCapture(self.file, display_filter="dns")
        for pkt in cap:
            print(pkt.highest_layer)

    def print_IP_info(self, pkt_num):
        print("Displaying basic IP info...")
        try:
            pkt = self.cap[pkt_num]
            print("IP Address:", pkt.ip.address)
            print("Source:", pkt.ip.src)
            print("Version:", pkt.ip.version)
        except:
            print("Nt valid packet number.")

    def print_http_info(self):
        try:

        except:
            print("May not contain http request...")