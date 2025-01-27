from packets.ARP import ARP
from Ethernet import *

#eth=Ethernet()
#eth.startCapturing("wlp4s0", lambda packet:  print(packet))
arp=ARP(interface="wlp4s0")
arp.setOperationType(type="request")
arp.setTargetIP(targetIp="10.42.0.215")

ether=Ethernet()
ether.setHeader(destMac="ff:ff:ff:ff:ff:ff",type=0x0806,interface="wlp4s0")
ether.setPayload(payload=arp.build())
ether.send()