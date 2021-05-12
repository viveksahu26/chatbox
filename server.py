#socket programing is a combination of ip and port no.
import socket
import os
import threading
#import function

#Need to specify which protocol to use.
# $$ udp protocol
my_protocol = socket.SOCK_DGRAM

#Ip Address comes under Address Family. Similarly, many different types of address comes under it. It will help to understand actually what is ip no.
# $$ net address family
afn = socket.AF_INET

#Socket requires 2 args, address family and protocol
sock = socket.socket( afn, my_protocol )

ip = "192.168.0.102"

#port no. is a way to identify the program remotely.
port = 1234

#bind ip with the port
sock.bind( (ip, port) )
		

def thread1():
	while True:
		data = sock.recvfrom(1024 )
		cmd = data[0].decode()
		clientip = data[1][0]
		clientPort = data[1][1]
		if cmd == "exit":
			break;
		print("\n\t\t\t\t\t" + clientip + ":" + cmd )

		msg = input("\n" + ip + ": ")
		sock.sendto(msg.encode(),(clientip,clientPort))
		if msg == "exit":
			break;	



x = threading.Thread( target=thread1 )

x.start()

