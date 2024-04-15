from socket import *
from ftplib import FTP, all_errors


# Creates a TCP socket
# SOCK_STREAM is used for TCP connections
clientSocket = socket(AF_INET, SOCK_STREAM)

#establish connection
def serverConnect(serverAddr, serverPort):
    clientSocket.connect((serverAddr, serverPort))
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
    with open(fname, "wb") as f:
        while True:
            text = clientSocket.recv(1024).decode()
            if not text:
                break
            f.write(text)

 

#upload file
def upload_file(clientSocket, fname):
    sendCommand(clientSocket, f'STOR {fname}\r\n')
    with open(fname, "rb") as f:
        while True:
            text = f.read(1024)
            if not text:
                break
            clientSocket.send(text)


# ftp.quit()

def main():

    #connecting
    sampleIP = "localhost"
    serverPort = 12000
    serverConnect(sampleIP, serverPort)
    
    while True:
        command = input("Enter command (CONNECT, LIST, RETRIEVE, STORE, QUIT): ")

        # Sending the command to the server
        sendCommand(clientSocket, command)

        if command.upper() == "QUIT":
            print("Closing connection on client end")
            clientSocket.close()
            break
        # #download file
        # download_file(clientSocket, "test.txt")

        

if __name__ == "__main__":
    main()
