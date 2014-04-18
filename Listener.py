#!/usr/bin/env python3
#-*- coding: utf-8 -*-
##############################################
# Home  : http://netkiller.github.io
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
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        #.decode(encoding='UTF-8')
        #socket.sendto(data.upper(), self.client_address)
        #socket.sendto(data, self.client_address)
        socket.sendto(data, self.client_address)
        print(self.client_address)

class LRRPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        #.decode(encoding='UTF-8')
        #socket.sendto(data.upper(), self.client_address)
        socket.sendto(data, self.client_address)		

class ARSHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        #.decode(encoding='UTF-8')
        #socket.sendto(data.upper(), self.client_address)
        socket.sendto(data, self.client_address)

def daemon(ip, port, headler):
	pid = os.fork()
	print(pid)
	if pid > 0:
		sys.exit(0)
	server = socketserver.UDPServer((ip, port), headler)
	server.serve_forever()
	pass
		
if __name__ == "__main__":
	try: 
		#if options.daemon:
		pid = os.fork()
		if pid == 0:
			print('Starting TMS Listener...')
			print("Child Process: PID# %s" % os.getpid() )
			HOST, PORT = "192.168.6.2", 4007
			tms = socketserver.UDPServer((HOST, PORT), TMSHandler)
			#tms.daemon = True
			tms.serve_forever()
		else:
			#sys.exit(0)
			pid = os.fork()
			if pid == 0:			
				print('Starting LRRP Listener...')
				print("Child Process: PID# %s" % os.getpid() )
				HOST, PORT = "192.168.6.2", 4001
				lrrp = socketserver.UDPServer((HOST, PORT), LRRPHandler)
				lrrp.serve_forever()
			else:
				#sys.exit(0)
				pid = os.fork()
				if pid == 0:			
					print('Starting ARS Listener...')
					print("Child Process: PID# %s" % os.getpid() )
					HOST, PORT = "192.168.6.2", 4005
					ars = socketserver.UDPServer((HOST, PORT), ARSHandler)
					ars.serve_forever()
				else:
					sys.exit(0)
		
	except OSError as err: 
		print(err)