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
except ImportError as err:
	print("Error: %s" %(err))    

class Mototrbo() :
	def __init__(self):
		usage = "usage: %prog [options] "
		self.parser = OptionParser(usage)

		self.parser.add_option('-c','--cai', dest="cai", metavar="12", help='CAI Network', default=12)
		
		group = OptionGroup(self.parser, "Utility", "Utility Programs")
		group.add_option("", "--id2ip", dest="id2ip", metavar="1001", default=None, help="Convert Radio ID to IP Address")		
		group.add_option('', "--ip2id", dest="ip2id", metavar="12.115.86.232", default=None, help="Convert IP Address to Radio ID")
		self.parser.add_option_group(group)
		
		#self.parser.add_option("-t", "--tms", dest="radioid", metavar="1001", default=None, help="Text Messaging Service (TMS)")
		#self.parser.add_option('','--clean', action="store_true", help='')
		#self.parser.add_option("-d", "--debug", action="store_true", help="Print debug information")
		group = OptionGroup(self.parser, "TMS", "Text Messaging Service (TMS)")
		group.add_option("-t", "--tms", dest="tms", metavar="1001", default=None, help="Radio ID")
		self.parser.add_option_group(group)
			
		#group.add_option("-d", "--delete", dest="delete", metavar="branch", help="delete branch")
		#group.add_option('','--release', dest="release", help='release version exampe:'+ time.strftime('%Y-%m-%d',time.localtime(time.time())) , default=None)
		
		group = OptionGroup(self.parser, "ARS", "Automatic Registration Service (ARS)")
		#group.add_option("-e", action="store_true", help="Print every action done")
		#group.add_option('-c','--cai', dest="cai", metavar="12", help='CAI Network', default=12)
		self.parser.add_option_group(group)
		
		group = OptionGroup(self.parser, 'LRRP', ' Location Request and Response Protocol (LRRP)')
		#group.add_option('-c','--cai', dest="cai", metavar="12", help='CAI Network', default=12)
		self.parser.add_option_group(group)
		
		#self.parser.add_option('-v','--version',action='store_true', help='print version number')
		#self.parser.add_option('-d','--daemon', dest='daemon', action='store_true', help='run as daemon')
		#self.parser.add_option('','--logfile', help='logs file.', default='backup.log')
		pass
	def tms(self):
		print('--------')
	def debug(self):
		print(unpack('B',b'\x14'))
		print(unpack('B',b'\x18'))
	def usage(self):
		self.parser.print_help()
		lines = [
			"\n  Example: ",
			"\t-c 12 -t 7558688 Hello",
			"\t--id2ip=1001",
			"\t--ip2id=12.115.86.232"
		]
		for line in lines:
			print(line)
		print("\n  Homepage: http://netkiller.github.io\tAuthor: Neo <netkiller@msn.com>")		
	def main(self):
		(self.options, args) = self.parser.parse_args()
		print("===================================")
		print(self.options, args)
		#self.usage()
		#print(self.config)
		print("===================================")
		if self.options.id2ip :
			protocol = Protocol()
			print(protocol.id2ip(int(self.options.id2ip)))
		if self.options.ip2id :
			protocol = Protocol()
			print(protocol.ip2id(str(self.options.ip2id)))
		if self.options.tms :
			tms = TMS()
			tms.sendtoid(int(self.options.cai), int(self.options.tms), args[0])
		else:
			self.usage()
		
if __name__ == '__main__':
	try:
		mototrbo = Mototrbo()
		mototrbo.main()
		

	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")
