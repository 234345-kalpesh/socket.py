import socket
s=socket.socket()
print("socket created") 
s.bind(('localhost',9999))
s.listen(3)
print("waiting for connection")
c,addr=s.accept()
while True:
    
    cmsg=c.recv(1024).decode()
    print(f"client-->>{cmsg}".rjust(60))
    if cmsg.lower()=="endofchat":
        print("session is end")
        c.close()
        break
    smsg=input("server-->").encode()
    c.send(smsg)
    if smsg.decode().lower()=="endof chat":
        print("session is end")
        c.close()
s.close()
