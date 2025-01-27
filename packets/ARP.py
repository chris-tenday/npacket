import struct
from utilities import *


class ARP:
    _hardwareType = struct.pack("!H", 1)  #ethernet
    _protocolType = struct.pack("!H", 0x0800)  #ipv4
    _hardwareSize = struct.pack("!B", 6)  #size of the mac address in bytes.
    _protocolSize = struct.pack("!B", 4)  #size of the protocol address to resolve (IPv4)

    opCode = None #specifies whether the ARP packet is an query or reply, or even reserve-arp
    senderMac = None
    senderIP = None
    targetMac = "00:00:00:00:00:00"
    targetIP = None
    _interface=None

    def __init__(self, interface):
        self._interface = interface
        '''if targetMac is None:
            self._targetMac = "00:00:00:00:00:00"
        else:
            self._targetMac = targetMac

        if senderMac is None:
            #get Interface Mac address
            self._senderMac = getInterfaceMac(interface=interface)
        else:
            self._senderMac = senderMac
        if senderIP is None:
            self._senderIP = getDeviceIP()
        else:
            self._senderIP = senderIP'''

    '''def generate(self):
        headerPart = struct.pack(
            "!HHBBH",
            self._hardwareType,
            self._protocolType,
            self._hardwareSize,
            self._protocolSize,
            self._opCode
        )

        header = headerPart + packMacAddress(self._senderMac) + packIP(self._senderIP) + packMacAddress(
            self._targetMac) + packIP(self._targetIP)
        self._packet = header

        return self._packet
    '''

    #set operation code (ARP query or reply)
    def setOpCode(self, opCode):
        self.opCode = struct.pack("!H", opCode)

    #set the target IP.
    def setTargetIP(self, targetIp):
        self.targetIP = packIP(targetIp)

    #Set the target Mac to resolve.
    def setTargetMac(self, mac):
        self.targetMac = packMacAddress(mac)

    #Set the sending device IP
    #By default: Device IP is used.
    def setSenderIP(self, senderIP):
        self.senderIP = packIP(senderIP)

    #Set the sending device Mac.
    #By default : Device interface Mac is used.
    def setSenderMac(self, mac):
        self.senderMac = packMacAddress(mac)

    #Build the packet.
    def build(self):
        self.senderIP = getDeviceIP() if self.senderIP is None else self.senderIP
        self.senderMac = getInterfaceMac(self._interface) if self.senderMac is None else self.senderMac

        packet = self._hardwareType + self._protocolType + self._hardwareSize + self._protocolSize + self.opCode
        '''packet += (packMacAddress(self.senderMac) + packIP(self.senderIP) + packMacAddress(self.targetMac)
                   + packIP(self.targetIP))'''
        return packet
