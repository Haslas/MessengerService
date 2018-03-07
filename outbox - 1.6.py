print("====OUTBOX====")
print("Version: 1.6")
import socket

def register():
    print("Connecting to server...")
    clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ip,outboxPort))
    print("Connection established")
    username = input("Enter username: ")
    clientsocket.send(bytes(username,"utf-8"))
    print("Username sent to server.")
    print("Waiting for reply from server")
    ack = clientsocket.recv(1024)
    print("Server reply recieved")
    ack = ack.decode("utf-8")
    if ack != "0":
            print("Username already taken.   Please choose another.")
            clientsocket.close()
            usernameAccepted=0
    else:
            print("Username Accepted")
            clientsocket.close()
            usernameAccepted=1
    return usernameAccepted


def registerLoop():
    usernameAccepted=0
    while not usernameAccepted:
        usernameAccepted=register()

def sendMessage():
    message=""
    while len(message) <1:
        message = input("Enter message: ")
    clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ip,outboxPort))
    clientsocket.send(bytes(message,"UTF-8"))
    clientsocket.close()




ip=input("IP Address: ")
outboxPort = ""
while type(outboxPort)!=int:
    outboxPort=input("Outbox Port: ")
    try:
        outboxPort=int(outboxPort)
    except ValueError:
        print("This should be a number.")
registerLoop()
while 1:
        sendMessage()
