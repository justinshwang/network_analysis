# FTP

import pyshark

pkts = pyshark.FileCapture('capturetest2.cap')

for packet in pkts:
    if 'FTP' in packet:
        try: 
            output = packet.ftp
            if 'USER' in str(output):
                print('__________')
                print('USERNAME:')
                print(output)
                print()
            elif 'PASS' in str(output):
                print('__________')
                print('PASSWORD:')
                print(output)
                print()
        except: 
            pass
        