print("====INBOX====")
print("Version: 1.6 - The Login")
import socket

def acceptConnection(serversocket):
        connection, address = serversocket.accept()
        buf = connection.recv(1024)
        buf = buf.decode("utf-8")
        print(buf)

def declareServerSocket(inboxPort):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(("",inboxPort))
        serversocket.listen(5)
        return serversocket


inboxPort=""
while type(inboxPort)!=int:
    inboxPort=input("Inbox Port: ")
    try:
        inboxPort=int(inboxPort)
    except ValueError:
        print("This should be a number.")
serversocket=declareServerSocket(inboxPort)      
while True:
        acceptConnection(serversocket)
