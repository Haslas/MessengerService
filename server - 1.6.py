print("===SERVER===")
print("Version: 1.6")
import socket
from datetime import datetime        

def compileMsg(message, user):
    now = datetime.now()
    timeStamp = "["+str(now.hour)+":"+str(now.minute)+"]"
    message = timeStamp+" "+user+": "+ message
    endMessage = bytes(message, "UTF=8")
    return endMessage

def sendMsg(ip,port,buf):
    if type(buf) != bytes:
        buf = bytes(buf,"utf-8")
    for num in range(0,5):
        try:
            clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientsocket.connect((ip,port))
            clientsocket.send(buf)
            print("Buf successfully sent")
            clientsocket.close()
            print("Socket closed")
            break
        except ConnectionRefusedError:
            print("Error sending to ip:",str(ip))
            print("Try:",str(num+1),"/ 5")
            if num == 4:
                print("----------------------")
                print("Address failed to respond")
                print("Removing Ip:",str(ip),"from list")
                userIP.remove(ip)
        

def replyMsg(connection,buf):
    sent=0
    print("Attempting to reply to client")
    buf = bytes(buf,"utf-8")
    for num in range(0,5):
        if sent==0:
            try:
                connection.send(buf)
                print("Responce succesfully sent.")
                sent=1
            except ConnectionRefusedError:
                print("Error replying to Ip:",str(ip))
                print("Try:",str(num+1),"/ 5")
                if num == 4:
                    print("----------------------")
                    print("Address failed to respond")
                    print("Removing Ip:",str(ip),"from list")
                    userIP.remove(ip)
    

def setupConn(ip,port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((ip,outboxPort))
    serversocket.listen(5)
    return serversocket

def recieveMsg(connection, address):
    buf = connection.recv(1024)
    buf = buf.decode("utf-8")
    print("Message recieved from outbox.")
    print("Data: "+buf)
    return buf

def acceptConnection(serversocket,userIP,users,inboxPort,outboxPort):
    connection, address = serversocket.accept()
    print("Connection found")
    print("Address: "+str(address))
    print("Ip recognised: ",end="")
    print(address[0] in userIP)
    if  address[0] in userIP:
        buf = recieveMsg(connection, address)
        buf = compileMsg(buf,users[address[0]])
        for user in userIP:
            sendMsg(user,inboxPort,buf)
        print("----------------------")
    else:
        buf = recieveMsg(connection, address)
        print("Attempting to reply to outbox, ip:",address[0])
        if buf in users:
            print("Username ("+buf+") not accepted.")
            replyMsg(connection,"1")
            print("----------------------")
        else:
            userIP.append(address[0])
            print("Username ("+buf+") accepted.")
            users[address[0]] = buf
            replyMsg(connection,"0")
            print("----------------------")


            

userIP = []
users={}
inboxPort = ""
while type(inboxPort)!=int:
    inboxPort=input("Inbox Port: ")
    try:
        inboxPort=int(inboxPort)
    except ValueError:
        print("This should be a number.")
outboxPort = ""
while type(outboxPort)!=int:
    outboxPort=input("Outbox Port: ")
    try:
        outboxPort=int(outboxPort)
    except ValueError:
        print("This should be a number.")
print("Ports Accepted")
serversocket=setupConn("",outboxPort)
while True:
    acceptConnection(serversocket,userIP,users,inboxPort,outboxPort)
