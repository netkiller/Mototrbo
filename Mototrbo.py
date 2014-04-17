#!/usr/bin/env python3
#-*- coding: utf-8 -*-
##############################################
# Home	: http://netkiller.github.io
# Author: Neo <netkiller@msn.com>
##############################################

try:
	from struct import *
except ImportError as err:
	print("Error: %s" %(err))	 

class Protocol():
	def __init__(self, buffer):
		self.buffer = buffer
	#def header(self):
		self.header = self.buffer[:6]
	#	return(self.header)
	#def message(self):
		self.message = self.buffer[6:]
	#	return(self.message)
	def id2ip(self, id):
		cai = '12'
		return (cai+"."+str((id >> 16) & 0xff) +'.'+ str((id >> 8) & 0xff) + '.' + str(id & 0xff));
	def ip2id(self, ipaddr):
		a, b, c, d = ipaddr.split('.');
		return ((int(b) << 16) + (int(c) << 8 ) + int(d));		
		
class TMS(Protocol):
	def __init__(self, buffer):
		super().__init__(buffer)
	def message_encode(self, msg):
		return(msg.encode('utf-16').replace(b'\xff\xfe', b'\x00'))

	def message_decode(self, msg = None):
		if msg :
			return( msg.replace(b'\x00', b'\xff\xfe', 1).decode('utf-16') )
		else:
			return( self.message.decode('utf-16') )
	def send(self, sms):
		return ( b'\x00\x14\xe0\x00\x88\x04\r\x00\n' + self.message_encode(sms) )

class ARS(Protocol):
	def __init__(self, buffer):
		self.buffer = buffer		

class LRRP(Protocol):
	def __init__(self, buffer):
		self.buffer = buffer		

class Mototrbo() :
	def __init__(self):
		print('--------')
	def tms(self):
		protocol = b'\x00\x14\xe0\x00\x88\x04\r\x00\n\x00B\x00G\x007\x00N\x00Y\x00T\x00'
		tms = TMS(protocol)
		print(tms.id2ip(7558888))
		print(tms.ip2id('12.115.86.232'))
		print(tms.message_encode('BG7NYT'))
		print(tms.message_decode(tms.message_encode('BG7NYT')))
		print(tms.message_decode())
		print(tms.send('Hello'))
		#.replace(b'\x00', b'')
		
		#header = protocol[:6]
		#message = protocol[9:]
		#print(tms.message_decode(message))
		
if __name__ == '__main__':
	try:
		mototrbo = Mototrbo()
		mototrbo.tms()
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")