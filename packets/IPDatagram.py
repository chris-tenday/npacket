import struct
from utilities import *
from packets.ICMP import *
from packets.Packet import *


class IPDatagram(Packet):
    version_header_length = struct.pack("!B",
                                        69)  #1-byte number representing both the IP datagram version(IPv4 + length of the header)
    dsfield = struct.pack("!B", 0)  #1-byte : differentiated services field.
    totalLength = None  #2-bytes : total length of the datagram (header length + payload length)
    identification = struct.pack("!H",random.randint(1,65535))  #2-bytes : identification number to match the datagram with a reply.
    flags = struct.pack("!H", 0)  #2-bytes : flags.
    ttl = struct.pack("!B", 64)  #2-bytes : time-to-live
    protocol = None  #1-byte : protocol of the payload.
    checksum = struct.pack("!H", 0)  #2-bytes : checksum covering the IP datagram header.
    sourceIp = None  #source IP.
    destIp = None  #dest IP.

    payload = None  #payload.

    def setSourceIP(self, ip):
        self.sourceIp = packIP(ip)

    def setDestIP(self, ip):
        self.destIp = packIP(ip)

    def _setChecksum(self, checksum):
        self.checksum = struct.pack("!H", checksum)

    def setPayload(self, payload):
        if isinstance(payload, ICMP) and issubclass(ICMP, Packet):
            self.protocol = struct.pack("!B", 1)  #ICMP protocol.
        else:
            raise Exception("[x] Protocol not supported.")
        self.payload = payload

    def _buildHeader(self):
        header = self.version_header_length + self.dsfield + struct.pack("!H", 20 + len(
            self.payload.build())) + self.identification + self.flags + self.ttl + self.protocol + self.checksum + self.sourceIp + self.destIp

        return header

    def build(self):
        header = self._buildHeader()
        check = calculateChecksum(header)
        self._setChecksum(checksum=check)
        header = self._buildHeader()

        return header + self.payload.build()
