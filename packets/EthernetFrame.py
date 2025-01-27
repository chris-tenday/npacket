from utilities import *
import struct
from packets.ARP import *


class EthernetFrame(Packet):
    _sourceMac = None  #source Mac address.(6-bytes)
    _destMac = None  #destination Mac address.(6-bytes)
    _frameType = None  #frame type (ARP,RARP or IP) (2-bytes)
    _payload = None  #frame payload
    _interface=None #network interface

    def __init__(self, interface):
        self._interface = interface

    '''Source Mac setting'''
    def setSourceMac(self, mac):
        self._sourceMac = packMacAddress(mac)

    '''Dest Mac setting'''
    def setDestMac(self, mac):
        self._destMac = packMacAddress(mac)

    '''Set the payload of the frame.'''
    def setPayload(self, payload):
        """
        set frame type based on the payload
        """
        if isinstance(payload, ARP) and issubclass(ARP, Packet):
            self._frameType = struct.pack("!H", 0x0806)
        elif type(payload) == "IPDatagram":
            self._frameType = struct.pack("!H", 2)
        else:
            raise Exception("Payload not supported.")
        self._payload = payload

    """
    Build and Get the packet.
    """
    def build(self):
        #fill source Mac
        self._sourceMac = packMacAddress(getInterfaceMac(self._interface)) if self._sourceMac is None else self._sourceMac

        packet = self._destMac + self._sourceMac + self._frameType + self._payload.build()
        return packet
