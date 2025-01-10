import struct


def checksum(data):
    #ensure the data length is even, pad with a zero byte if necessary
    if len(data) % 2 !=0:
        data+=b'\0'
    #Sum 16-bit words
    total=0
    for i in range(0,len(data),2):
        #convert two bytes to one 16-bit word
        word=struct.unpack("!H",data[i:i+2])[0]
        total+=word
        #keep the result to 16-bits by carrying over the overflow
        total=(total & 0xffff) + (total >> 16)

    check=~total & 0xffff
    return check