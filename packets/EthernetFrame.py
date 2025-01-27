from utilities import *
import struct


class EthernetFrame:
    _sourceMac = None  #source Mac address.
    _destMac = None  #destination Mac address.
    _frameType = None  #frame type (ARP,RARP or IP)
    _payload = None #frame frame payload

    def __init__(self, interface,payload):
        #Set the device Mac as the source Mac by default.
        self._sourceMac = getInterfaceMac(interface=interface)
        #set frame type based on the payload
        if type(payload) == "ARPFrame":
            self._frameType = struct.pack("!H", 1)
        elif type(payload) == "IPDatagram":
            self._frameType = struct.pack("!H", 2)
        else:
            raise Exception("Payload not supported.")

    #Source Mac setting
    def setSourceMac(self, mac):
        self._sourceMac = packMacAddress(mac)

    #Dest Mac setting
    def setDestMac(self, mac):
        self._destMac = packMacAddress(mac)

    #Build and Get the packet.
    def getPacket(self):
        packet = self._destMac + self._sourceMac + self._frameType
        return packet
