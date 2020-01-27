# OSPF

import pyshark

pkts = pyshark.FileCapture('capturetest2.cap')

for packet in pkts:
    if 'OSPF' in packet:
        print('OSPF password: ' + packet.ospf.auth_simple)