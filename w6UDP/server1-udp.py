

import socket

port_number = 5555
server_ip = '127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((server_ip,port_number))


while True:
	(msg,addr) = s.recvfrom(1024)
	msg = msg.decode('ascii')
	print("Got {} from {}".format(msg,addr))
	updated = msg + " that is a horrible idea"
	updated = updated.encode('ascii')
	s.sendto( updated, (addr) )