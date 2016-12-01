#!/usr/bin/env python3
#-*- coding: utf-8 -*-
##############################################
# Home	: http://netkiller.github.io
# Author: Neo <netkiller@msn.com>
##############################################

try:
	from struct import *
	from optparse import OptionParser, OptionGroup
	from Protocol import *
	import socketserver, os, sys
except ImportError as err:
	print("Error: %s" %(err))	 


class TMSHandler(socketserver.BaseRequestHandler):

	protocol = Protocol()
	

	def handle(self):
		data = self.request[0]
		#.strip()
		socket = self.request[1]
		print("{} wrote:".format(self.client_address[0]))
		#print(self.client_address)
		tms = TMS(data)
		#print(data)
		#print(data.decode(encoding='UTF-16'))
		print(tms.decode())
		#socket.sendto(data.upper(), self.client_address)
		#socket.sendto(data, self.client_address)
		#socket.sendto(data, self.client_address)
		
if __name__ == "__main__":
	try: 

		print('Starting TMS Listener...')
		print("Child Process: PID# %s" % os.getpid() )
		HOST, PORT = "192.168.11.2", 4007
		tms = socketserver.UDPServer((HOST, PORT), TMSHandler)
		#tms.daemon = True
		tms.serve_forever()
		#tms = TMS()
		#tms.debug()

	except OSError as err: 
		print(err)
