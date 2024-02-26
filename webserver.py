#Yang Lu 114607667 CSE 310 Assignment 1 Part 1
from socket import *

host = '127.0.0.1'  #localhost
serverPort = 8000

serverSocket = socket(AF_INET,SOCK_STREAM) #creating the socket
serverSocket.bind((host, serverPort))

serverSocket.listen(1) #listen for connections
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept() # accept incoming connections
    request = connectionSocket.recv(1024).decode() #receives the http request
    
    htmlfile = request.split()[1][1:] #this extracts out the name of hello.html

    try:
        with open(htmlfile, 'rb') as hello: #opening the html file
            responseData = hello.read() #reading the html content
            response = "HTTP/1.1 200 OK\r\n\r\n".encode() + responseData

    except:  #if theres no html file found
        response = "HTTP/1.1 404 Not Found\r\n\r\nError 404 Page Not Found".encode() 
    
    connectionSocket.sendall(response) #send response back
    connectionSocket.close()
