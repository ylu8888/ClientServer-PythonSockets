"""In this part of the assignment, you will learn the basics of socket programming for TCP
connections in Python: how to create a socket, bind it to a specific address and port, as well as
send and receive a HTTP packet. You will also learn some basics of HTTP header format.
Develop a web server that handles one HTTP request at a time. Your web server should be able
to (a) accept and parse the HTTP request, get the requested file from the server’s file system, (b)
create an HTTP response message consisting of the requested file preceded by header lines, and
then (c) send the response directly to the client. (d) If the requested file is not present in the
server, the server should send an HTTP “404 Not Found” message back to the client."""
