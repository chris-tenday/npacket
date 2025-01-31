from layers.Ethernet import *
from packets.EthernetFrame import *
from layers.IP import *
from packets.ICMP import *

icmp=ICMP()
icmp.setPayload(payload="Carmelle Tenday")

datagram=IPDatagram()
datagram.setSourceIP(ip="10.42.0.1")
datagram.setDestIP(ip="10.42.0.215")
datagram.setPayload(payload=icmp)

ip=IP()
ip.setDatagram(datagram=datagram)
ip.send()






