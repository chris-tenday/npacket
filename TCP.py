import random
import struct
from utilities import calculateChecksum


class TCP:
    sourcePort=None
    destPort=None
    sequenceNumber=None #inital sequence number
    ackNumber=None
    flags=None
    window=None
    payload=None

    #Set the segment header.
    def setHeader(self,destPort,flags,sourcePort=None,sequenceNumber=None,ackNumber=None,window=None):
        self.destPort=destPort
        if sourcePort is None:
            self.sourcePort=random.randint(5000,65535)
        else:
            self.sourcePort=sourcePort

        if sequenceNumber is None:
            self.isn=1
        else:
            self.sequenceNumber=sequenceNumber

        if ackNumber is None:
            self.ackNumber=2 #acking byte 1 and expecting the next byte
        else:
            self.ackNumber=ackNumber

        if window is None:
            self.window=1460
        else:
            self.window=window

    def setPayload(self,payload):
        self.payload=payload

    def generate(self):
        header=struct.pack(
            "!HHIIHHHH",
            self.sourcePort,
                self.destPort,
                self.sequenceNumber,
                self.ackNumber,
                0, #TODO: Group these fields in a 2-bytes value : header length(4bits) + reserved(3bits) + flags(9bits)
                self.window,
                0, #checksum
                0
        )
        header[18:]=15
        #put together the header & payload.
        packet= header + self.payload


    def checksum(self,header,payload):
        return calculateChecksum(header + payload)

