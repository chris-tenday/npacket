from packets.ARP import ARP
from Ethernet import *

#eth=Ethernet()
#eth.startCapturing("wlp4s0", lambda packet:  print(packet))
arp=ARP(interface="wlp4s0")
arp.setOpCode(opCode=1)
arp.setTargetIP(targetIp="10.42.0.215")

ether=Ethernet()
ether.setHeader(destMac="ff:ff:ff:ff:ff:ff",type=1,interface="wlp4s0")
ether.setPayload(payload=arp.build())
ether.send()