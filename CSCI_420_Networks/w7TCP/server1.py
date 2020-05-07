import socket

port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( ("127.0.0.1",port))
s.listen(10)

while True:
	print("Waiting for accept")
	client_socket, addr = s.accept()
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