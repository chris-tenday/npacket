import random
import socket
import struct
from checksum import *
from utilities import *

'''
Class for crafting an IP Datagram
'''


class IP:
    _sourceIp = None
    _destIp = None
    _payload = None
    _protocol = None
    _identification = None
    _ttl = None
    _packet = None

    #Set the datagram header.
    def setHeader(self, destIp, protocol, sourceIp=None, identification=random.randint(1, 65535), ttl=32):
        self._destIp = destIp
        self._protocol = protocol
        self._identification = identification
        self._ttl = ttl
        if sourceIp is None:
            # Get device IP.
            self._sourceIp = socket.gethostbyname(socket.gethostname())
        else:
            self._sourceIp = sourceIp

    #Set the payload of the datagram
    def setPayload(self, payload):
        self._payload = payload  # in bytes

    #Build and generate the IP Datagra,
    def _generate(self):
        # craft the IP Header without the checksum set
        header = self._buildHeader()
        #calculate the checksum.
        check = checksum(header)
        #update the checksum in the header.
        header = self._buildHeader(checksum=check)

        self._packet = header + self._payload

    def _buildHeader(self, checksum=0):
        header = struct.pack(
            "!BBHHHBBH",
            69,  # version + header length
            0,  # dsfield
            20 + len(self._payload),  # total length
            self._identification,  # identification field
            0,  # flags + fragment field
            self._ttl,  # ttl field
            self._protocol,  # protocol field
            checksum,  # checksum
        )
        return header + packIP(self._sourceIp) + packIP(self._destIp)

    #send the IP Datagram
    def send(self):
        if self._payload is None:
            print("[x] No Payload set.")
        self._generate()
        # IP layer raw socket.
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        sock.sendto(self._packet, (self._destIp, 0))

    '''
    Start capturing packet based on a specified protocol
    '''
    def startCapture(self,protocol):
        sock=socket.socket(socket.AF_INET, socket.SOCK_RAW, protocol)
        sock.bind(("10.42.0.1", 0))
        while 1:
            print("Waiting for a packet....")
            packet = sock.recvfrom(65535)
            print("captured packet")
