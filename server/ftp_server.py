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

def serverConnect(serverAddr, serverPort):
    clientSocket.connect((serverAddr, serverPort))
    return clientSocket

def listFiles():
    files = os.listdir('.')
    return '\n'.join(files)

def sendResponse(clientSocket):
    response = "Command received and processed"
    clientSocket.send(response.encode())

while True:
    # Accepting connections from the client
    clientSocket, addr = tcpSocket.accept()
    print(f"Connection from {addr}")
    
    while True:
        # Receiving the command from the client
        command = clientSocket.recv(1024).decode()
        print(f"Received command: {command}")
        #print(f"Waiting for a new command...")
    
        if command.upper() != "QUIT":
            print(f"Waiting for a new command...")

        if command.upper() == "QUIT":
            print("Terminating connection")
            clientSocket.close()
            break

        if command.upper().startswith("CONNECT"):
            ipAddr = command.split()[1]
            portNum = int(command.split()[2])
            clientSocket = serverConnect(ipAddr, portNum)
            sendResponse(clientSocket)
            

        if command.upper() == "LIST":
            fileList = listFiles()
            clientSocket.send(fileList.encode())
            sendResponse(clientSocket)
    
        
        elif command.upper().startswith("STORE"):
            fname = command.split()[1]
            with open(fname, "w") as f:
                while True:
                    data = clientSocket.recv(1024).decode()
                    if "\t\t\t" in data:    
                        data = data.replace("\t\t\t", "")
                        f.write(data)
                        break
                    f.write(data)
            sendResponse(clientSocket)
        
        elif command.upper().startswith("RETRIEVE"):
            fname = command.split()[1]
            if os.path.exists(fname):
                with open(fname, "rb") as f:
                    data = f.read()
                    clientSocket.sendall(data)
            else:
                print("File doesn't exist")
                
    clientSocket.close()
    break

tcpSocket.close()