"""
name: chris
date: 2/25/20
desc: tcp server with threading
"""
import socket
import threading

def TCPworker(sockets):

	client_socket,addr = sockets[-1]
	print(addr)
	print("There are {} things in socket_list".format(len(socket_list)))
	while True:
		msg = client_socket.recv(1024)
		if not msg:
			print("client disconnect")
			break
		print("got: {}".format(msg))
		msg = msg.decode('ascii')
		msg = msg.decode('ascii') + " haha!"
		for other_soc, other_addr in sockets:
			if client_socket, addr != other_soc, other_addr : 
				print("Sending to {}".format(other_addr))
				other_soc.sendall(msg.encode('ascii'))
		client_socket.sendall(msg.encode('ascii'))
	sockets.remove( (client_socket, addr) )

port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_list = []
s.bind( ("127.0.0.1",port))
s.listen()

while True:
	print("Waiting for accept")
	client_socket, addr = s.accept()
	socket_list.append( (client_socket,addr) )
	print("adding {} to socket list".format(addr))
	thread = threading.Thread(target = TCPworker, args= [socket_list] )
	thread.start()
	with client_socket:
		print("Got connect from {}".format(addr))
		while True:
			msg = client_socket.recv(1024)
			if not msg:
				print("Client disconnect")
				break
			print("Got: {}".format(msg))
			msg = msg.decode('ascii') + " Haha!"
			client_socket.sendall(msg.encode('ascii'))