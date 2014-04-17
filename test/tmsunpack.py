# nc -ul 127.0.0.1 5005
from struct import *
pack('c', 'B')
str = pack('6s', b'BG7NYT')
print(repr(str))

print(unpack('hhl', b'\x00\x14\xe0\x00\x88\x04\r\x00\n\x00B\x00G\x007\x00N\x00Y\x00T\x00'))
print(unpack('4h', b'\x00\x14\xe0\x00\x88\x04\r\x00\n'))
print(unpack('6s', b'\x00B\x00G\x007\x00N\x00Y\x00T\x00'))
print(unpack('1x1s', b'\x00B'))
B
b'\x00B'.decode(encoding='UTF-8')
callsign = b'\x00B\x00G\x007\x00N\x00Y\x00T\x00'
callsign.replace(b'\x00', b'')

callsign.decode('hex')

callsign.encode('utf-8')

#split('\x00', 1)
protocol = b'\x00\x0e\xe0\x00\x82\x04\r\x00\n\x00E\x00e\x00e\x00'
protocol = b'\x00\x14\xe0\x00\x88\x04\r\x00\n\x00B\x00G\x007\x00N\x00Y\x00T\x00'
header = protocol[:6].replace(b'\x00', b'')
print(header)
header[2:1]
unpack('4B',header)
print(unpack('ii', header))


#
dlen = unpack('H', header[0:2])
print(dlen)

opa = unpack('B', header[0:1])
print(opa)
opb = unpack('B', header[2:3])
print(opb)


"""
192.168.11.1 wrote:
b'\x00\x08\xe0\x00\x81\x04\r\x00\n\x00'
192.168.11.1 wrote:
b'\x00\x03\xbf\x00\x01'
192.168.11.1 wrote:
b'\x00\x0e\xe0\x00\x82\x04\r\x00\n\x00E\x00e\x00e\x00'
192.168.11.1 wrote:
b'\x00\x03\xbf\x00\x02'
192.168.11.1 wrote:
b'\x00\x0e\xe0\x00\x85\x04\r\x00\n\x00E\x00e\x00e\x00'
192.168.11.1 wrote:
b'\x00\x03\xbf\x00\x05'

空数据
b'\x00\x08\xe0\x00\x86\x04\r\x00\n\x00'
192.168.11.1 wrote:
b'\x00\x03\xbf\x00\x06'
192.168.11.1 wrote:
b'\x00\x08\xe0\x00\x87\x04\r\x00\n\x00'
192.168.11.1 wrote:
b'\x00\x03\xbf\x00\x07'

BG7NYT
192.168.11.1 wrote:
b'\x00\x14\xe0\x00\x88\x04\r\x00\n\x00B\x00G\x007\x00N\x00Y\x00T\x00'
192.168.11.1 wrote:
b'\x00\x03\xbf\x00\x08'
"""



