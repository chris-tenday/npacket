import struct
from utilities import *
from packets.Packet import *


class ARP(Packet):
    _hardwareType = struct.pack("!H", 1)  #ethernet
    _protocolType = struct.pack("!H", 0x0800)  #ipv4
    _hardwareSize = struct.pack("!B", 6)  #size of the mac address in bytes.
    _protocolSize = struct.pack("!B", 4)  #size of the protocol address to resolve (IPv4)

    opCode = None  #specifies whether the ARP packet is an query or reply, or even reserve-arp
    senderMac = None
    senderIP = None
    targetMac = "00:00:00:00:00:00"
    targetIP = None
    _interface = None

    def __init__(self, interface):
        self._interface = interface

    '''set operation code (ARP query or reply)'''
    def setOpCode(self, opCode):
        self.opCode = struct.pack("!H", opCode)

    '''
    Specify the ARP operation type (request, reply or reverse) by means of a string.
    '''
    def setOperationType(self, type="request"):
        if type == "request":
            self.opCode = 1
        elif type == "reply":
            self.opCode = 2
        self.opCode = struct.pack("!H", self.opCode)

    '''
    set the target IP.
    '''
    def setTargetIP(self, targetIp):
        self.targetIP = packIP(targetIp)

    '''Set the target Mac to resolve.'''
    def setTargetMac(self, mac):
        self.targetMac = packMacAddress(mac)

    '''Set the sending device IP
    By default: Device IP is used.
    '''
    def setSenderIP(self, senderIP):
        self.senderIP = packIP(senderIP)

    '''Set the sending device Mac.
    By default : Device interface Mac is used.
    '''
    def setSenderMac(self, mac):
        self.senderMac = packMacAddress(mac)

    '''Build the packet.'''
    def build(self):
        self.senderIP = packIP(getDeviceIP()) if self.senderIP is None else self.senderIP
        self.senderMac = packMacAddress(getInterfaceMac(self._interface)) if self.senderMac is None else self.senderMac

        packet = (self._hardwareType + self._protocolType + self._hardwareSize + self._protocolSize + self.opCode
                  + self.senderMac + self.senderIP + packMacAddress(self.targetMac) + self.targetIP)
        return packet
