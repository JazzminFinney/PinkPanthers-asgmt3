from socket import *
import os

# Creates a TCP socket
# SOCK_STREAM is used for TCP connections
tcpSocket = socket(AF_INET, SOCK_STREAM)

# Binding localhost and a port number to the socket
tcpSocket.bind(('localhost', 12000))
 
# Listening for requests from the client
tcpSocket.listen(5)
print('The server is listening on port 12000')

def listFiles():
    files = os.listdir('.')
    return '\n'.join(files)

def sendReponse(clientSocket):
    response = "Command received and processed"
    clientSocket.send(response.encode())

while True:
    # Accepting connections from the client
    clientSocket, addr = tcpSocket.accept()
    print(f"Connection from {addr}")
    
    # Receiving the command from the client
    command = clientSocket.recv(1024).decode()
    print(f"Received command: {command}")
    print(f"Waiting for a new command...")
    
    
    if command.upper() == "LIST":
        fileList = listFiles()
        clientSocket.send(fileList.encode())
        sendReponse(clientSocket)
        
    elif command.upper().startswith("STORE"):
        fname = command.split()[1]
        with open(fname, "wb") as f:
            while True:
                data = clientSocket.recv(1024)
                if not data:
                    break
                f.write(data)
        sendReponse(clientSocket)

    elif command.upper() == "QUIT":
        print("Terminating connection")
        clientSocket.close()
        break
