from layers.Ethernet import *
from packets.EthernetFrame import *


#eth.startCapturing("wlp4s0", lambda packet:  print(packet))

#Build the ARP request packet.
arp=ARP(interface="wlp4s0")
arp.setOperationType(type="request")
arp.setTargetIP(targetIp="10.42.0.215")

ethernetFrame=EthernetFrame(interface="wlp4s0")
ethernetFrame.setDestMac("ff:ff:ff:ff:ff:ff")
ethernetFrame.setPayload(payload=arp)

eth=Ethernet(interface="wlp4s0")
eth.setFrame(frame=ethernetFrame)
eth.send()










#ether=Ethernet()
#ether.setHeader(destMac="ff:ff:ff:ff:ff:ff",type=0x0806,interface="wlp4s0")
#ether.setPayload(payload=arp.build())
#ether.send()
