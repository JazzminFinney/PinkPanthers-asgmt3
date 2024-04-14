from socket import *
from ftplib import FTP, all_errors

#abby - let's see if i can push

# Creates a TCP socket
# SOCK_STREAM is used for TCP connections
clientSocket = socket(AF_INET, SOCK_STREAM)

#establish connection
def serverConnect(serverAddr, serverPort):
    clientSocket.connect(serverAddr, serverPort)
    return clientSocket
'''ftp = FTP()
ftp.connect(ip_addr, port)
ftp.login(user, password) '''

def sendCommand(clientSocket, command):
    clientSocket.send(command.encode())
    response = clientSocket.recv(1024).decode()
    print(response)
    
#download file    
#not completely sure if this is using sendCommand correctly
def download_file(clientSocket, fname):
    sendCommand(clientSocket, f'RETR {fname}\r\n')
    with open(fname, wb) as f:
        while True:
            text = clientSocket.recv(1024).decode()
            f.write(text) 

 

#upload file
def upload_file(clientSocket, fname):
    sendCommand(clientSocket, f'RETR {fname}\r\n')
    with open(fname, rb) as f:
        while True:
            text = f.read(1024)
            clientSocket.send(text)


ftp.quit()

def main():
    
    while True:
        command = input("Enter command (CONNECT, LIST, RETRIEVE, STORE, QUIT): ")

        #connecting
        sampleIP = "10.0.0.1"
        clientSocket = serverConnect(sampleIP, 21)

        # Sending the command to the server
        sendCommand(clientSocket, command)

        #download file
        download_file(clientSocket, "test.txt")

        

if __name__ == "__main__":
    main()
