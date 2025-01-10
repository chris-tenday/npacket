import os
import struct
import subprocess


#Calculate the checksum
def calculateChecksum(data):
    #ensure the data length is even, pad with a zero byte if necessary
    if len(data) % 2 != 0:
        data += b'\0'
    #Sum 16-bit words
    total = 0
    for i in range(0, len(data), 2):
        #convert two bytes to one 16-bit word
        word = struct.unpack("!H", data[i:i + 2])[0]
        total += word
        #keep the result to 16-bits by carrying over the overflow
        total = (total & 0xffff) + (total >> 16)

    check = ~total & 0xffff
    return check


#Take an IP in string form and pack it into a 4-bytes object.
def packIP(ip):
    ipBytes = bytes()
    for n in ip.split("."):
        ipBytes += struct.pack("B", int(n))
    return ipBytes


#Get an interface Mac address.
def getInterfaceMac(interface):
    file = open(f'/sys/class/net/{interface}/address')
    mac = file.read().replace(" ", "").replace("\n", "")
    return mac


#Take a Mac address in string form and pack it into a 6-bytes object.
def packMacAddress(mac):
    macBytes = bytes.fromhex(mac.replace(":", ""))
    packed = bytes()
    for b in macBytes:
        packed += struct.pack("!B", b)

    return packed


#Get device current IP.
def getDeviceIP():
    res = subprocess.run(["hostname", "-I"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ip = res.stdout.strip().decode()
    return ip


#Display some text on the console.
def display(text, type="info"):
    icon="[!] "
    if type == "error":
        icon="[x] "
    print(icon+text)
