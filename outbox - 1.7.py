print("====OUTBOX====")
print("Version: 1.6 - The Login")
import socket
ip="10.110.211.179"
inboxPort = 666

#===================================================================#
"""
def setupServerConn(ip,port):
    global serversocket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((ip,port))
    serversocket.listen(5)
"""
    
def onConnect():
            print("Connecting to server...")
            clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientsocket.connect((ip,inboxPort))
            print("Connection established")
            username = input("Enter username: ")
            clientsocket.send(bytes(username,"utf-8"))
            print("Username sent to server.")
            print("Second server connection established")
            print("Waiting for reply from server")
            ack = clientsocket.recv(1024)
            print("Server reply recieved")
            ack = ack.decode("utf-8")
            if ack != "0":
                    print("Username already taken.   Please choose another.")
                    clientsocket.close()
                    onConnect()
            else:
                    print("Username Accepted")
                    clientsocket.close()

#===================================================================#

#RUN FROM YOUR PROBLEMS

onConnect()

message=""
while 1:
        while len(message) <1:
            message = input("Enter message: ")
        clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((ip,inboxPort))
        clientsocket.send(bytes(message,"UTF-8"))
        clientsocket.close()
        message=""
