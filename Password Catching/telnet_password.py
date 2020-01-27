# OSPF

import pyshark

pkts = pyshark.FileCapture('capturetest2.cap')

for packet in pkts:
    if 'TELNET' in packet:
        try:
            output = packet.telnet
            if 'Username' in str(output):
                print('_________________')
                print('USERNAME:')
            elif 'Password' in str(output):
                print('_________________')
                print('PASSWORD:')
                
            if packet.telnet.data:
                print(output)
        
        except:
            pass