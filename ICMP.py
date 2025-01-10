import random

from checksum import *
'''
Class for crafting ICMP packet.
'''
import struct
from checksum import *

class ICMP:
    _type=None
    _code=None
    _identifier=None
    _sequenceNumber=None
    _payload=None

    def __init__(self,type,payload,identifier=random.randint(1,65535),sequenceNumber=random.randint(1,65535),code=0):
        self._type=type
        self._code=code
        self._identifier=identifier
        self._sequenceNumber=sequenceNumber
        self._payload=payload #in bytes

    #Build and generate the complete ICMP packet.
    def generate(self):
        #initially the checksum is set to 0
        header=self._buildHeader(checksum=0)
        #calculate the checksum
        check=checksum(header + self._payload)
        #update the checksum in the header.
        header=self._buildHeader(checksum=check)

        #return the complete ICMP packet.
        return header + self._payload

    #Handle the checksum setting in the header.
    def _buildHeader(self,checksum=0):
        header = struct.pack(
            "!BBHHH",
            self._type,  # type field
            self._code,  # code field.
            checksum,  # checksum
            self._identifier,  # identifier field
            self._sequenceNumber,  # sequence number field
        )
        return header

