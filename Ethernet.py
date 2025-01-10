import socket
import struct
from utilities import *

class Ethernet:
    _sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    _sourceMac = None
    _destMac = None
    _type = None
    _interface = None
    _payload = None
    _packet = None

    #Set the frame header.
    def setHeader(self, destMac, type, interface, sourceMac=None):
        self._destMac = destMac
        self._type = type
        self._interface = interface
        if sourceMac is None:
            self._sourceMac = getInterfaceMac(interface=interface)
        else:
            self._sourceMac = sourceMac

    #Set the frame payload
    def setPayload(self, payload):
        self._payload = payload

    def _generate(self):
        headerPart = struct.pack(
            "!H",
            self._type
        )

        header = packMacAddress(self._destMac) + packMacAddress(self._sourceMac) + headerPart
        self._packet = header + self._payload

    #Send the frame
    def send(self):
        if self._payload is None:
            print("[x] No payload set.")
            return
        self._generate()
        self._sock.bind((self._interface, 0))
        self._sock.send(self._packet)

    def startCapturing(self,interface,callback):
        sock=socket.socket(socket.AF_PACKET, socket.SOCK_RAW,socket.htons(0x0003))
        sock.bind(("wlp4s0",0))
        while 1:
            packet=sock.recv(65535)
            #call the callback
            callback(packet)
