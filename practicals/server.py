#!/usr/bin/python3

import sys
import socket


# Server function

def server(ServerIPAddress, ServerPortNumber) : 

    # Server's IPAddress and PortNumber
    ServerPair = (ServerIPAddress, ServerPortNumber)

    # Create a listening socket
    ListenSocket = socket.socket()

    # Bind the listening socket to that pair
    ListenSocket.bind(ServerPair)

    QueueLength = 1
    
    # Execute "listen" function
    ListenSocket.listen(QueueLength)

    print("Server listening at ", ServerPair)

    # If a connection request comes in, accept that request by executing the accept function
    ClientHandleSocket, ClientPair = ListenSocket.accept()

    print("Connected to client at ", ClientPair)

    # Receive data sent by Client
    ClientData = ClientHandleSocket.recv(10000)
    ClientData = ClientData.decode('utf-8')

    print("Client: ", ClientData)
    
    ServerData = "Hey! This is the server :)"
    ServerData = bytes(ServerData.encode('utf-8'))

    # Send Server data
    ClientHandleSocket.send(ServerData)

    print("\n")
    # Close the socket handling the client 
    ClientHandleSocket.close()
    print("Socket handling the Client closed")

    # Close the listening socket (Usually, this is not done)
    ListenSocket.close()
    print("Socket listening to incoming connections closed")


if __name__ == "__main__" : 

    if len(sys.argv) != 3 : 
        print("Usage: $ ", sys.argv[0], " <ServerIPAddress> <ServerPortNumber>")
        sys.exit()

    ServerIPAddress = sys.argv[1]
    ServerPortNumber = int(sys.argv[2])

    # Call the function
    server(ServerIPAddress, ServerPortNumber)

