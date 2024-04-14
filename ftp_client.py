from socket import *

#abby - let's see if i can push

# Creates a TCP socket
# SOCK_STREAM is used for TCP connections
clientSocket = socket(AF_INET, SOCK_STREAM)

def sendCommand(clientSocket, command):
    clientSocket.send(command.encode())
    response = clientSocket.recv(1024).decode()
    print(response)
    
def main():
    
    while True:
        command = input("Enter command (CONNECT, LIST, RETRIEVE, STORE, QUIT): ")

        # Sending the command to the server
        sendCommand(clientSocket, command)

if __name__ == "__main__":
    main()