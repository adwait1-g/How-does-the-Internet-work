#!/usr/bin/python3

import sys
import socket


# Server function 

def client(ServerIPAddress, ServerPortNumber) : 

    # Server's IPAddress and PortNumber
    ServerPair = (ServerIPAddress, ServerPortNumber)

    # Create a socket
    ClientSocket = socket.socket()

    # Connect to server
    ClientSocket.connect(ServerPair)
    print("Connected to ", ServerPair)

    # Type in some data to send to server
    SendData = str(input("Type Something: "))
    SendData = bytes(SendData.encode('utf-8'))
    # Send data to server
    ClientSocket.send(SendData)

    # Receive data from server
    ServerData = ClientSocket.recv(10000)
    ServerData = ServerData.decode('utf-8')

    print("Server: ", ServerData)

    print("Client job done!")

    # Close the socket
    ClientSocket.close()



if __name__ == "__main__" : 

    if len(sys.argv) != 3 : 
        print("Usage: $ ", sys.argv[0], " <ServerIPAddress> <ServerPortNumber>")
        sys.exit()

    ServerIPAddress = sys.argv[1]
    ServerPortNumber = int(sys.argv[2])

    # Call the function
    client(ServerIPAddress, ServerPortNumber)
