from socket import *
from ftplib import FTP, all_errors
import os


# Creates a TCP socket
# SOCK_STREAM is used for TCP connections
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(5.0)

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

def receiveList(clientSocket):
    fileList = ""
    while True:
        #print("testing")
        try:
            text = clientSocket.recv(1024).decode()
            print(text)
            fileList += text
        except timeout:
            print("End of data")
            break
    print("Files in the server directory:")
    print(fileList)
    
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
        if command.upper() == "LIST":
            sendCommand(clientSocket, command)
            receiveList(clientSocket)
        
        elif command.upper() == "STORE":
            fname = input("Enter name of file to store: ")
            sendCommand(clientSocket, f"{command} {fname}")
            upload_file(clientSocket, fname)
            
        elif command.upper() == "RETRIEVE":
            fname = input("Enter name of file to retrieve: ")
            sendCommand(clientSocket, f"{command} {fname}")
            download_file(clientSocket, fname)
    
        elif command.upper() == "QUIT":
            sendCommand(clientSocket, command)
            print("Closing connection on client end")
            clientSocket.close()
            break
        # #download file
        # download_file(clientSocket, "test.txt")
        
        else:
            print("Invalid command")

        

if __name__ == "__main__":
    main()
