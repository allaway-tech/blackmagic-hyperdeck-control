import socket
import connections
import commands

hyperdeck = connections.Hyperdeck()
hyperdeckControl = commands.Hyperdeck()
BUFFER_SIZE = 2048

for x in hyperdeck.addresses:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((x, hyperdeck.port))
	s.send(hyperdeckControl.stop)
	s.send(hyperdeckControl.quit)
	data = s.recv(BUFFER_SIZE)
	s.close

	print "Received data:\n\n", data
