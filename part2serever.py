import socket
import datetime
serverIP = '192.168.1.107'  # our server IP 
port = 5051 #port number
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverIP,port))
# Set the socket to broadcast mode
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
print("Server is ready to receive.....")
print("   Taleen Bayatneh   ")#this peer just recieve mesages no send
peers = set()
try:
    while True:
        message, client_address = serverSocket.recvfrom(1024)
        print(f"Received message from {message.decode()} AT {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ")
        print("===================================")  
        #this loop is to send the message for all peers excpet the sender 
        for addr in peers:
            if addr != client_address:
                serverSocket.sendto(message, addr)
        #this is for adding the peer to the set of peers
        peers.add(client_address) 
except KeyboardInterrupt:
    print("the server will be closed.......")
finally:
    serverSocket.close()