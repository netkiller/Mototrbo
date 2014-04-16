# nc -ul 127.0.0.1 5005
import socket

UDP_IP = "192.168.11.1"
UDP_PORT = 4007
#MESSAGE = "Hello, World!"
#MESSAGE = b'\x00\x14\xe0\x00\x88\x04\r\x00\n\x00B\x00G\x007\x00N\x00Y\x00T\x00'
MESSAGE = b'\x00\x14\xe0\x00\x88\x04\r\x00\n\x00B\x00D\x007\x00N\x00Y\x00T\x00'

#print "UDP target IP:", UDP_IP
#print "UDP target port:", UDP_PORT
#print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
