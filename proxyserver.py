\#Yang Lu 114607667 CSE 310 Assignment 1 Part 2

#caching making a file out of the response
#check ur local files to see if its there
#use with OPEN function
#proxy server is basically a server and a client
#with an extra port on it, where you create files
from socket import *

#host = '127.0.0.1'  #localhost
proxyPort = 8000
serverPort = 80   

serverSocket = socket(AF_INET,SOCK_STREAM) #creating the socket
serverSocket.bind(('', proxyPort))

serverSocket.listen(1) #listen for connections
print('The PROXY Server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept() # accept incoming connections

    request = connectionSocket.recv(4096).decode() #receives the http request
    htmlfile = request.split()[1][1:] #this extracts out the name of hello.html
    #delimiter splits into words, the URL is usually the second element, 1: takes the entire string onward
    print('this is the html file', htmlfile)

    #make a socket for both the proxy and the server
    #look in ur own cache, look if whatever they requested, google for example, if its not in ur own cache like u dont have a local file of google,
    #then you ask the webserver then you ask the other connection then thats when u make another connection with port 80
    #get that respones, put it in a file, so next time they make a request asking for google, u already have it on hand
    #and give it to them from the cache

    try: #CHECKING IF THE CLIENT REQUEST IS IN THE CACHE
        with open(htmlfile, 'rb') as cache:
            responseData = cache.read()
            response = "HTTP/1.1 200 OK\r\n\r\n".encode() + responseData 
            #response = "HTTP/1.1 200 OK\r\n\r\n".encode()
            print('WE FOUND THE FILES IN THE CACHE')

    except: #IF ITS NOT IN THE CACHE WE HAVE TO ASK THE WEBSERVER
        try:

            ipAddress = gethostbyname(htmlfile)
            print('this is the address', ipAddress) 
            secondSocket = socket(AF_INET, SOCK_STREAM)
            secondSocket.connect((ipAddress, serverPort))  #connect the google URL with PORT 80
            print('connected to the other server')

            secondSocket.sendall(request.encode())  #send cleint request, have to encode because its a string
            
            response = secondSocket.recv(4096)
            secondSocket.close()

            #SAVING IT INTO THE CACHE
            with open(htmlfile, 'wb') as cache:
                cache.write(response) 
                print('SUCCESSFULLY SAVED INTO THE CACHE')

        except:
            response = "HTTP/1.1 404 Not Found\r\n\r\nError 404 Page Not Found".encode() 
            print('WE CANNOT CONNECT TO THE SERVER')

    connectionSocket.sendall(response)
    connectionSocket.close()
