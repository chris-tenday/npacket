import struct
from utilities import *


class ARP:
    _hardwareType = 1 #ethernet
    _protocolType = 0x0800 #ipv4
    _hardwareSie = 6
    _protocolSize = 4
    _opCode = None
    _senderMac = None
    _senderIP = None
    _targetMac = None
    _targetIP = None
    _packet = None

    def __init__(self, opCode, interface, targetIP, targetMac=None, senderMac=None, senderIP=None):
        self._opCode = opCode
        self._targetIP = targetIP
        if targetMac is None:
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
            self._senderIP = senderIP

    def generate(self):
        headerPart = struct.pack(
            "!HHBBH",
            self._hardwareType,
            self._protocolType,
            self._hardwareSie,
            self._protocolSize,
            self._opCode
        )
        header = headerPart + packMacAddress(self._senderMac) + packIP(self._senderIP) + packMacAddress(
            self._targetMac) + packIP(self._targetIP)
        self._packet = header
        return self._packet
