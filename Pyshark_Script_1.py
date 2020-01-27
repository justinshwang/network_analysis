import pyshark

pkts = pyshark.FileCapture('capturetest2.cap')

for pkt in pkts:
    try:
        print('Source = ' + packet['ip'].src)
        print('Destination = ' + packet['ip'].dst)
    except:
        pass
        
print("Finished!")
exit()