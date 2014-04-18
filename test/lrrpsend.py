# nc -ul 127.0.0.1 5005
import socket

UDP_IP = "192.168.11.1"
#UDP_IP = "12.115.86.12"
UDP_PORT = 4001

# command 0xf disabled lrrp
#MESSAGE = b'\x2204\x3727\x1707\x0f'
# command 0x9
MESSAGE = b'\x2204\x3727\x1707\x5074\x6934\x31\x01\x09'


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
