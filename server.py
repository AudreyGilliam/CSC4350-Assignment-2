#Audrey Gilliam
#Server

from socket import *
serverPort = 8000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print ("The server is ready to recieve")

    
while True:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024).decode()

    connectionSocket.send(sentence.upper().encode())

    connectionSocket.close()
