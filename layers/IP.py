import socket

from packets.IPDatagram import *


class IP:
    _datagram = None #datagram to send.


    def setDatagram(self,datagram):
        self._datagram = datagram

    def send(self):
        if not isinstance(self._datagram, IPDatagram):
            print("[x] Invalid Datagram.")
        # IP layer raw socket.
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        res=sock.sendto(self._datagram.build(), ("10.42.0.215", 0))
