import socketserver

class LRRP(socketserver.BaseRequestHandler):

    def setup(self):
        print("{} is connected!".format(self.client_address))
        #self.request.send('Hello ' + str(self.client_address) + '\n')
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        idata = map(ord, data)
        print(idata)
        #.decode(encoding='UTF-8')
        #socket.sendto(data.upper(), self.client_address)
        #socket.sendto(data, self.client_address)
    def finish(self):
        print( "{} disconnected".format(self.client_address) )
        #self.request.send('bye client %s\n' % str(self.client_address))
if __name__ == "__main__":
    HOST, PORT = "192.168.11.2", 4001
    server = socketserver.UDPServer((HOST, PORT), LRRP)
    server.serve_forever()


"""
b'f &\x04\xc6Q\x1aUB'
b'f %\xb8\x83Q\x1aV\x10'

b'f &&-Q\x1aI\xe0'
b'f %\xc8AQ\x1aDK'
b'f &\x03RQ\x1aLR'
b'f &\x00\x15Q\x1aMK'
b'f &\x00\xceQ\x1aK\xe2'
b'f %\xffMQ\x1aM\x06'
b'f %\xfe\x18Q\x1aLb'
b'f %\xfc\xc8Q\x1aN\x95'
b'f &\x046Q\x1aW\xa9'
b'f %\xf3\x91Q\x1a`\x87'
b'f %\xf0?Q\x1a`k'
b'f %\xfb\xb1Q\x1aI\x95'

b'\x027\x10'
b'\x027\x10'
b'f &m-Q\x1ab\x8f'
b'f &,\xd0Q\x1aZ\x82'
b'f &$\xf8Q\x1aY;'
b'f &!\x90Q\x1aY\x8a'
b"f &'kQ\x1aeG"

b'f &\x9c\xf4Q\x1aq\x9d'
b'f %\xc8\xe6Q\x1ab\x8e'
b'f %\xc8\xe6Q\x1ab\x8e'

b'f %\xd6\xbaQ\x1aP%'
b"f %\xe1'Q\x1aRu"
b'f %\xc6\x07Q\x1aQ\x07'
"""
