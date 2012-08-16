from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor, defer
from twisted.internet.task import LoopingCall

class Client(LineReceiver):
	end="Close connection"
	def connectionMade(self):
		self.sendLine("User connected")
		self.sendLine(self.end)
		
	def lineReceived(self, line):
		print "recieve:", line
		if line == self.end:
			self.transport.loseConnection()					
class ClientFactory(ClientFactory):
    protocol = Client

    def clientConnectionFailed(self, connector, reason):
        print 'connection failed:', reason.getErrorMessage()
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print 'connection lost:', reason.getErrorMessage()
        reactor.stop()
