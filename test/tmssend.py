# nc -ul 127.0.0.1 5005
import socket

UDP_IP = "192.168.11.1"
UDP_IP = "12.115.86.12"
UDP_PORT = 4007

#MESSAGE = b'\x00\x0e\xe0\x00\x83\x04\r\x00\n\x00E\x00e\x00e\x00'
#MESSAGE = b'\x00\x18\xe0\x00\x88\x04\r\x00\n\x00B\x00G\x007\x00N\x00Y\x00T\x00T\x00U\x00'
#MESSAGE = b'\x01\x14\xe0\x00\x88\x04\r\x00\n\x00B\x00H\x007\x00N\x00Y\x00T\x00'
#MESSAGE = b'\x00\x16\xe0\x00\x8f\x04\r\x00\n\x00\nN\xf0S\x0c\xff|T\xebS\xa8`\x020'
MESSAGE = b'\x00\x12\xe0\x00\x88\x04\r\x00\n\x00H\x00e\x001\x00l\x00l\x00'
#print "UDP target IP:", UDP_IP
#print "UDP target port:", UDP_PORT
#print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
