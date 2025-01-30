from abc import ABC
from packets.Packet import *
import struct
import random
from utilities import *


class ICMP(Packet):
    type = struct.pack("!B", 8)  # 1-byte : representing the ICMP packet type(8 -> echo request, 0 -> echo reply.)
    code = struct.pack("!B", 0)  # 1-byte
    checksum=struct.pack("!H",0) #cheksum before calculation.
    identifier = struct.pack("!H", random.randint(1, 65535))  # 2-bytes : used for matching an ICMP reply and request.
    sequenceNumber = struct.pack("!H", 1)  # 2-bytes

    payload = None  #ICMP payload.

    '''
    Set ICMP type (8 -> for Echo requesst , 0 -> for Echo reply)
    '''
    def setType(self, type = "request"):
        if type == "request":
            self.type=struct.pack("!B",8)
        elif type == "reply":
            self.type=struct.pack("!B",0)
        else:
            raise Exception("[x] ICMP Type not supported.")

    '''
    Set checksum
    '''
    def _setChecksum(self,checksum):
        self.checksum=struct.pack("!H",checksum)

    '''
    Set payload.
    '''
    def setPayload(self, payload):
        self.payload = payload.encode()

    '''
    Build the header.
    '''
    def _buildHeader(self):
        header = self.type + self.code + self.checksum + self.identifier + self.sequenceNumber
        return header

    """
    Build the packet.
    """
    def build(self):
        header = self._buildHeader()
        #calculate checksum.
        checksum = calculateChecksum(header + self.payload)
        self._setChecksum(checksum=checksum)
        header = self._buildHeader()

        return header + self.payload
