print("====INBOX====")
print("Version: 1.5 - The Login")
import socket
inboxPort = 5996

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
        
serversocket=declareServerSocket(inboxPort)      
while True:
        acceptConnection(serversocket)

   
