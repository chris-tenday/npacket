from layers.Ethernet import *
from packets.EthernetFrame import *
from IP import *
from packets.ICMP import *

icmp=ICMP()
icmp.setPayload(payload="Chris Tenday")

ip=IP()
ip.setHeader(destIp="10.42.0.215",protocol=1,sourceIp="10.42.0.1")
ip.setPayload(payload=icmp.build())
ip.send()










#ether=Ethernet()
#ether.setHeader(destMac="ff:ff:ff:ff:ff:ff",type=0x0806,interface="wlp4s0")
#ether.setPayload(payload=arp.build())
#ether.send()
