import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "192.168.0.101"
port = 4321
sock.bind((ip, port))
while True: 
    msg = input("\n" + ip + ": " )
    serverip = "192.168.0.102"
    serverport = 1234
    sock.sendto(msg.encode() , (serverip, serverport))
    if msg == "exit":
        break;
    
    data = sock.recvfrom(1024)
    cmd = data[0].decode() 
    
    if cmd == "exit":
        break;
    print("\n\t\t\t\t" + serverip + ": " + cmd)