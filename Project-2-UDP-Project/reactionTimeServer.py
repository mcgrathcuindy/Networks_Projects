import socket

port_number = 5555
server_ip = '0.0.0.0'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((server_ip, port_number))

while True:
    print("Waiting for a packet!")
    (msg1, addr1) = s.recvfrom(1024)
    msg1 = msg1.decode('ascii')
    print("Message 1 recieved, with a time of {}.".format(msg1))
    (msg2, addr2) = s.recvfrom(1024)
    msg2 = msg2.decode('ascii')
    print("Message 2 recieved, with a time of {}.".format(msg2))

    #if ident1 != ident2:
    if msg1 < msg2:
        print("The person with the fastest reaction time was {}, with a time of {}".format(addr1, msg1))
    else:
        print("The person with the fastest reaction time was {}, with a time of {}".format(addr2, msg2))
