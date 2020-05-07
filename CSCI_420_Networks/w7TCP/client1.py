"""
Name: Chris McGrath
Date: 2/25/20
Desc: client1 TCP
"""

import socket

port = 5555 # sent to port above 1024

host = socket.gethostname()
host = '127.0.0.1'
print("I am {}".format(host))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect( (host, port))
	while True:
		message = input("What do you want to send?")
		#s.send(message.encode('ascii'))
		if message == 'exit':
			break
	s.sendall(message.encode('ascii'))
	print("message Sent!")
	rcv = s.recv(1024)
	print("Got: {}".format(rcv.decode('ascii')))
	s.close()
