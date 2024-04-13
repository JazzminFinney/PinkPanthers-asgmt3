from socket import *

# Creates a TCP socket
# SOCK_STREAM is used for TCP connections
tcpSocket = socket(AF_INET, SOCK_STREAM)

# Binding localhost and a port number to the socket
tcpSocket.bind(('localhost', 12000))

# Listening for requests from the client
tcpSocket.listen(5)
print('The server is listening on port 12000')

while True:
    # Accepting connections from the client
    clientSocket, addr = tcpSocket.accept()
    
    # Receiving the command from the client
    command = clientSocket.recv(1024).decode()