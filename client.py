#Audrey Gilliam
#Client 

from socket import *
serverName = "127.0.0.1"
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)

'''#constant for menu
QUIT_CHOICE = 4

#menu function for client
def menu():
    print("MENU")
    print("1: IP Address and Method")
    print("2: Port")
    print("3: Time Delay")
    print("4: QUIT")

#default choice
choice = 0

#while user does not want to quit, ask for input
while choice!= QUIT_CHOICE:
    menu()
    #ask for user input
    choice = int(input("Please enter the number corresponding with the menu item wanted: "))

    clientSocket.connect((serverName.serverPort))
    clientSocket.send(choice.encode())'''


message = input("Input lowercase sentence: ")

clientSocket.connect((serverName, serverPort))
clientSocket.send(message.encode())

modifiedMessage = clientSocket.recv(1024)
print (modifiedMessage.decode())
clientSocket.close




    
