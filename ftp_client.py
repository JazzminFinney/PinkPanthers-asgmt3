from socket import *
from ftplib import FTP, all_errors
import os


# Creates a TCP socket
# SOCK_STREAM is used for TCP connections
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(5.0)

def sendCommand(clientSocket, command):
    clientSocket.send(command.encode())

def receiveList(clientSocket):
    fileList = ""
    while True:
        try:
            text = clientSocket.recv(1024).decode()
            fileList += text
        except timeout:
            #print("End of data")
            break
    fileList = fileList.replace("Command received and processed", "")  #remove the response
    print(fileList)
    
#download file    
def download_file(clientSocket, fname): 
    sendCommand(clientSocket, f'RETR {fname}\r\n')
    text = ""
    while True:
        try:
            new_data = clientSocket.recv(1024).decode()
            if new_data == '':
                break
            text += new_data
        except error:
            print("End of data")
            break
    with open(fname, "w") as f:
        f.write(text)

#upload file
def upload_file(clientSocket, fname):
    #sendCommand(clientSocket, f'STOR {fname}\r\n')
    with open(fname, "rb") as f:
        while True:
            text = f.read(1024)
            if not text:
                break
            clientSocket.send(text)
    clientSocket.send("\t\t\t".encode())    #end of file
    print(f"Uploaded {fname}")


def main():
    
    is_connected = False
    
    while True:
        if not is_connected:
            command = input("Enter command (CONNECT): ")
        else:
            command = input("Enter command (LIST, RETRIEVE, STORE, QUIT): ")

        # Sending the command to the server
        if command.upper() == "CONNECT":
            ipaddr = input("Enter IP Address of server to connect to: ")
            port = int(input("Enter port number: "))
            # sendCommand(clientSocket, f"{command} {ipaddr} {port}")
            clientSocket.connect((ipaddr, port))
            print("You are now connected")
            is_connected = True
            
        if is_connected:

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
    
        if command.upper() == "QUIT":
            sendCommand(clientSocket, command)
            print("Closing connection on client end")
            clientSocket.close()
            break
        
        elif not is_connected and command.upper() != "CONNECT":
            print("Invalid command")

        

if __name__ == "__main__":
    main()
